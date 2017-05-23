#coding:GBK
import os,sys,time,re,subprocess,logging,unittest,util
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from  selenium.webdriver.support.ui import WebDriverWait
import log
reload(sys)
sys.setdefaultencoding('GBK')
global driver,Testtime
localpath = os.getcwd()
sys.path.append(localpath)
def finddevices():
    rst = os.popen('adb devices').readlines()
    devices = ''.join(rst)
    devices =  devices.count("device")
    if devices > 1:
        print ('共找到%s个手机'%(devices-1))
        return True
    else:
        print ('没有找到手机，请连接后再重试！')
def duo_finddevices():
    logger = util.logger
    rst = util.exccmd('adb devices')              # 结合util文件看，相当于执行os.popen('adb devices').read()  返回adb devices的执行结果
    devices = re.findall(r'(.*?)\s+device',rst)   # 如果有两台设备执行结果为：['List of', '0123456789ABCDEF', '0123456789ABCDEF']
    if len(devices) > 1:
        deviceIds = devices[1:]                            #从第二个元素开始截取列表 （devices上面得到的结果为：['List of', '0123456789ABCDEF', '0123456789ABCDEF']，从第二个位置开始取也就是取到设备ID）那么deviceIds得到的值就是设备ID号（得到的值一行一个不带引号）
        logger.info('共找到%s个手机！'%str(len(devices)-1))  # 写入到LOG内，如上，列表内3个值，要减一个才是真实的设备数
        for i in deviceIds:
            logger.info('ID为%s'%i)    # 写入到LOG内，迭代打印
        return deviceIds               # 输出并保存返回的值
    else:
        logger.error('没有检测到手机，请检查')
        return
def cleanEnv():
    '''每次执行命令时就把此TestResult目录删除,然后再新建TestResult,相当于清空上次的测试结果和日志
    '''
    os.system('adb kill-server')
    needClean = ['log.log','img','TestResult']   # 定义这=log.log,img,TestResult这三个值
    pwd = os.getcwd()                     # pwd=当前文件目录
    for i in needClean:                   # 循环needClean
        delpath = os.path.join(pwd,i)     # 结果为：当前目录\img和当前目录\TestResult  （例：C:\Users\Administrator\Desktop\测试结果\img）
        if os.path.isfile(delpath):
            cmd = 'del /f/s/q "%s"'% delpath   # 删除delpath得到的两个文件夹（img和TestResult）/F 强制删除只读文件/S 从所有子目录删除指定文件/Q 安静模式。删除全局通配符时，不要求确认。
            os.system(cmd)
        elif os.path.isdir(delpath):       # 否则，删除delpath得到的两个文件夹（img和TestResult）
            cmd = 'rd /s/q "%s"' %delpath
            os.system(cmd)
    if not os.path.isdir('TestResult/screenshot'):
     #   os.makedirs('TestResult')
        os.makedirs('TestResult/screenshot/Failed')
        os.makedirs('TestResult/screenshot/Passed')
cleanEnv() #让导入此文件时就执行清除件和新建文件
def getdevices():
    '''返回设备信息供需要时使用。devicename,andriodVersion,deviceModelName
    '''
    devicedetals = []
    #获取测试机SN名称
    deviceSN = os.popen('adb shell getprop ro.serialno'.format(localpath))
    '''下面加上去掉\r\n是为了去掉：如：deviceName":"8a8084a344417920308\r\n"
    '''
    devicename = deviceSN.readlines()[0].strip('\r\n')
#   devicename =  "'%s'"%eval('devicename') #转换为带引号的字符串 如：Android 转换为：'Android'
    devicedetals.append(devicename)
    #获取系安卓系统版本号
    version = os.popen('adb shell getprop ro.build.version.release'.format(localpath))
    andriodVersion = version.readlines()[0].strip('\r\n')
#   andriodVersion =  "'%s'"%eval('andriodVersion')#转换为带引号的字符串
    devicedetals.append(andriodVersion)
    #获取测试机机型设备名称
    deviceModel = os.popen('adb shell getprop ro.product.model'.format(localpath))
    deviceModelName = deviceModel.readlines()[0]
#   deviceModelName =  "'%s'"%eval('deviceModelName')#转换为带引号的字符串
    devicedetals.append(deviceModelName)

    '''
    #获取包名  (要使用此项请先把AAPT添加到环境变量)
    badging = os.popen('aapt dump badging C:\\Users\\Administrator\\Desktop\\12308.apk'.format(localpath))

#    badging 是一个对象，用readline()读取第一行用分隔提取
#    获取的值如下：
#    package: name='com.wxws.myticket' versionCode='61' versionName='6.1.1'

    packagename = badging.readline().split("'")[1]
    devicedetals.append(packagename)
    '''

    return devicename,andriodVersion,deviceModelName  # 此处暂时不返回：packagename
def start_Appium(host, port, bootstrap_port, appium_log_path):
    '''命令方法后台启动APPIUM
    用法：start_Appium('localhost','4723','4780','rst/appium.log')
    '''
    errormsg = ""
    appium_server_url =""
    cmd ='start /b appium -a '+ host +' -p '+ str(port)+ ' --bootstrap-port '+ str(bootstrap_port) +  ' --session-override --log '+ '"'+appium_log_path + '" --command-timeout 600'  #' -U '+ device_uid+
        #p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #stdout=PIPE, stderr=PIPE)
#    p = subprocess.call(cmd, shell=True,stdout=open('E:/logs.log','w'),stderr=subprocess.STDOUT)
    p = subprocess.call(cmd, shell=True,stdout=open('TestResult\\cmdlogs.log','w'),stderr=subprocess.STDOUT)
    print p
    appium_server_url = 'http://' + host +':' + str(port) +'/wd/hub'
    time.sleep(5)
    print '启动APPIUM服务完成，访问的URL地址为：%s'%appium_server_url
def stop_Appium(Appium_url):
        #stop_Appium('http://127.0.0.1:4723/wd/hub')
        a = Appium_url.split(":")[2].split("/")[0]
        cmd = 'netstat -aon | findstr %s'%a
        p = os.popen(cmd).readlines()    #执行当前目录的BAT文件必须用system,用os.popen(cmd)就不行
        if p:  #判断列表不为空时
            p = ''.join(p).split('LISTENING')[1].split()[0].strip()#以LISTENING来判断真正的PID，避免TIME_WAIT或ESTABLISHED状态
            cmd = 'taskkill /f /pid %s'%p
            os.popen(cmd)
            print '执行关闭APPIUM服务命令成功，PID为：%s'%p
        else:
            print 'kill APPIUM服务失败，传入的端口号是 %s ，请检查是否开启或端口是否不一致！'%a
