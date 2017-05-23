#coding:GBK
import unittest,ctypes,cmd,traceback,logging,unittest,os,sys,time,re,MySQLdb,requests,xlrd,time,ntplib,datetime,subprocess
from ConfigParser import ConfigParser
localpath1 = os.getcwd()+'\\bin'
localpath2 = os.getcwd()+'\\plugins'
localpath3 = os.getcwd()+'\\Case'
sys.path.append(localpath1)
sys.path.append(localpath2)
sys.path.append(localpath3)
import Initialization,glob,log,HTMLTestRunner,util,SettingDevice,gettime
from appium import webdriver
from find import *

reload(sys)
sys.setdefaultencoding('GBK')
localpath = os.getcwd()
sys.path.append(localpath)

def finddevices():
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
def doInstall(deviceids,host, port, bootstrap_port, appium_log_path):

    count = len(deviceids)               # 获取手机的列表的长度，保存到count
    port_list = range(4723,4723+count)   # 如果count等于3，那么port_list输出值为：4723,4724,4725
    bootstrap_port = range(4780,4780+count)   #如果count等于3，那么port_list输出值为：4780,4781,4782
    for i in range(len(deviceids)):
        cmd ='start /b appium -a '+ host +' -p '+ str(port_list[i])+ ' --bootstrap-port '+ str(bootstrap_port[i]) +  ' --session-override --log '+ '"'+appium_log_path + '" --command-timeout 600'
        p = subprocess.call(cmd, shell=True,stdout=open('TestResult\\cmdlogs.log','w'),stderr=subprocess.STDOUT)
        SettingDevice.Setting_device()
        #subprocess.Popen('start /b appium -a '+ host +' -p '+ str(port_list[i])+ ' --bootstrap-port '+ str(bootstrap_port[i]) +  ' --session-override --log '+ '"'+appium_log_path + " --command-timeout 600")
        driver = webdriver.Remote('http://' + host +':'+str(port_list[i])+'/wd/hub',desired_caps)
        util.doInThread(load_tests,deviceids[i])    #此处结果 deviceids = ['0123456789ABCDEF'] d = <uiautomator.AutomatorDevice object at 0x01BE1530> installapk = <function installapk at 0x01F91D70>
        # 这里用多线程方式执行了installapk函数
def start_appium(deviceids,host,appium_log_path):

    count = len(deviceids)               # 获取手机的列表的长度，保存到count
    port_list = range(4723,4723+count)   # 如果count等于3，那么port_list输出值为：4723,4724,4725
    bootstrap_port = range(4780,4780+count)   #如果count等于3，那么port_list输出值为：4780,4781,4782
    for i in range(len(deviceids)):
        cmd ='start /b appium -a '+ host +' -p '+ str(port_list[i])+ ' --bootstrap-port '+ str(bootstrap_port[i]) +  ' --session-override --log '+ '"'+appium_log_path + '" --command-timeout 600'
        p = subprocess.call(cmd, shell=True,stdout=open('TestResult\\cmdlogs.log','w'),stderr=subprocess.STDOUT)
        print('启动服务：http://' + host +':'+str(port_list[i])+'/wd/hub')
    time.sleep(5)   #等待服务启动
def util_start_appium(ip):
    for i in range(len(ip)):
        subprocess.Popen('start /b appium -a '+ host +' -p '+ str(4723+2*i)+ ' --bootstrap-port '+ str(bootstrap_port) +  ' --session-override --log '+ '"'+appium_log_path + '" --command-timeout 600')
        time.sleep(3.5)
        dingwei = webdriver.Remote("http://localhost:"+str(4723+2*i)+"/wd/hub", desired_caps)
        dingwei = DingWei(wzj, name)
        t = threading.Thread(target=dingwei.begin)
        tt.append(t)
def load_tests():
    #logger加到此处eclispe才有日志输出加到这里也可以
 #   logger = log.Logger('TestResult/log.log',clevel = logging.INFO,Flevel = logging.INFO)
    test_file_strings = glob.glob(r'Case\\test_*.py')
    module_strings = [str[5:len(str)-3] for str in test_file_strings]# Case\test_登录流程.py 从第5个开始取到倒数第三个至 结果：test_登录流程
    print '共获取到以下Case!'
    for Case in module_strings:
        print Case
    caseList = '\n'.join(module_strings)
    suites = [unittest.defaultTestLoader.loadTestsFromName(str) for str in module_strings]
    testSuite = unittest.TestSuite(suites)
    return testSuite
if __name__ == '__main__':
    logger = util.logger          # 开启线程LOG跟踪
    deviceids = finddevices()
    try:
            start_appium(deviceids,'localhost',"TestResult//appium.log")
            time.sleep(5)
        #if Initialization.finddevices() == True and gettime.EffectiveTime()==True: # 检查是否已连接上手机并且联网认证OK
            #start_appium(deviceids,'localhost',"TestResult//appium.log")
            #Initialization.start_Appium('localhost','4723','4780','TestResult//appium.log')# 启动APPIUP服务
            timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            filename ='TestResult\\result_'+ timestr + '.html'   #保存在TestResult目录下
            fp =open(filename,'wb')
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'报告明细')
            runner.run(load_tests())
            fp.close()
            logging.shutdown()
            Initialization.stop_Appium('http://localhost:4723/wd/hub')
            print '测试完成，详情请查看测试报告 %s'%filename
    except Exception,e:
        f=open("Errorlog.log","wb")
        traceback.print_exc(file=f)
        f.flush()
        f.close()
        traceback.print_exc()
    cmd_1 = 'taskkill /F /IM node.exe'
    os.popen(cmd_1).readlines()
    print '结束node进程成功！'
    thisIsLove = raw_input('按 ENTER 键退出窗口！')