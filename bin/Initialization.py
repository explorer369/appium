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
        print ('���ҵ�%s���ֻ�'%(devices-1))
        return True
    else:
        print ('û���ҵ��ֻ��������Ӻ������ԣ�')
def duo_finddevices():
    logger = util.logger
    rst = util.exccmd('adb devices')              # ���util�ļ������൱��ִ��os.popen('adb devices').read()  ����adb devices��ִ�н��
    devices = re.findall(r'(.*?)\s+device',rst)   # �������̨�豸ִ�н��Ϊ��['List of', '0123456789ABCDEF', '0123456789ABCDEF']
    if len(devices) > 1:
        deviceIds = devices[1:]                            #�ӵڶ���Ԫ�ؿ�ʼ��ȡ�б� ��devices����õ��Ľ��Ϊ��['List of', '0123456789ABCDEF', '0123456789ABCDEF']���ӵڶ���λ�ÿ�ʼȡҲ����ȡ���豸ID����ôdeviceIds�õ���ֵ�����豸ID�ţ��õ���ֵһ��һ���������ţ�
        logger.info('���ҵ�%s���ֻ���'%str(len(devices)-1))  # д�뵽LOG�ڣ����ϣ��б���3��ֵ��Ҫ��һ��������ʵ���豸��
        for i in deviceIds:
            logger.info('IDΪ%s'%i)    # д�뵽LOG�ڣ�������ӡ
        return deviceIds               # ��������淵�ص�ֵ
    else:
        logger.error('û�м�⵽�ֻ�������')
        return
def cleanEnv():
    '''ÿ��ִ������ʱ�ͰѴ�TestResultĿ¼ɾ��,Ȼ�����½�TestResult,�൱������ϴεĲ��Խ������־
    '''
    os.system('adb kill-server')
    needClean = ['log.log','img','TestResult']   # ������=log.log,img,TestResult������ֵ
    pwd = os.getcwd()                     # pwd=��ǰ�ļ�Ŀ¼
    for i in needClean:                   # ѭ��needClean
        delpath = os.path.join(pwd,i)     # ���Ϊ����ǰĿ¼\img�͵�ǰĿ¼\TestResult  ������C:\Users\Administrator\Desktop\���Խ��\img��
        if os.path.isfile(delpath):
            cmd = 'del /f/s/q "%s"'% delpath   # ɾ��delpath�õ��������ļ��У�img��TestResult��/F ǿ��ɾ��ֻ���ļ�/S ��������Ŀ¼ɾ��ָ���ļ�/Q ����ģʽ��ɾ��ȫ��ͨ���ʱ����Ҫ��ȷ�ϡ�
            os.system(cmd)
        elif os.path.isdir(delpath):       # ����ɾ��delpath�õ��������ļ��У�img��TestResult��
            cmd = 'rd /s/q "%s"' %delpath
            os.system(cmd)
    if not os.path.isdir('TestResult/screenshot'):
     #   os.makedirs('TestResult')
        os.makedirs('TestResult/screenshot/Failed')
        os.makedirs('TestResult/screenshot/Passed')
cleanEnv() #�õ�����ļ�ʱ��ִ����������½��ļ�
def getdevices():
    '''�����豸��Ϣ����Ҫʱʹ�á�devicename,andriodVersion,deviceModelName
    '''
    devicedetals = []
    #��ȡ���Ի�SN����
    deviceSN = os.popen('adb shell getprop ro.serialno'.format(localpath))
    '''�������ȥ��\r\n��Ϊ��ȥ�����磺deviceName":"8a8084a344417920308\r\n"
    '''
    devicename = deviceSN.readlines()[0].strip('\r\n')
#   devicename =  "'%s'"%eval('devicename') #ת��Ϊ�����ŵ��ַ��� �磺Android ת��Ϊ��'Android'
    devicedetals.append(devicename)
    #��ȡϵ��׿ϵͳ�汾��
    version = os.popen('adb shell getprop ro.build.version.release'.format(localpath))
    andriodVersion = version.readlines()[0].strip('\r\n')
#   andriodVersion =  "'%s'"%eval('andriodVersion')#ת��Ϊ�����ŵ��ַ���
    devicedetals.append(andriodVersion)
    #��ȡ���Ի������豸����
    deviceModel = os.popen('adb shell getprop ro.product.model'.format(localpath))
    deviceModelName = deviceModel.readlines()[0]
#   deviceModelName =  "'%s'"%eval('deviceModelName')#ת��Ϊ�����ŵ��ַ���
    devicedetals.append(deviceModelName)

    '''
    #��ȡ����  (Ҫʹ�ô������Ȱ�AAPT��ӵ���������)
    badging = os.popen('aapt dump badging C:\\Users\\Administrator\\Desktop\\12308.apk'.format(localpath))

#    badging ��һ��������readline()��ȡ��һ���÷ָ���ȡ
#    ��ȡ��ֵ���£�
#    package: name='com.wxws.myticket' versionCode='61' versionName='6.1.1'

    packagename = badging.readline().split("'")[1]
    devicedetals.append(packagename)
    '''

    return devicename,andriodVersion,deviceModelName  # �˴���ʱ�����أ�packagename
def start_Appium(host, port, bootstrap_port, appium_log_path):
    '''�������̨����APPIUM
    �÷���start_Appium('localhost','4723','4780','rst/appium.log')
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
    print '����APPIUM������ɣ����ʵ�URL��ַΪ��%s'%appium_server_url
def stop_Appium(Appium_url):
        #stop_Appium('http://127.0.0.1:4723/wd/hub')
        a = Appium_url.split(":")[2].split("/")[0]
        cmd = 'netstat -aon | findstr %s'%a
        p = os.popen(cmd).readlines()    #ִ�е�ǰĿ¼��BAT�ļ�������system,��os.popen(cmd)�Ͳ���
        if p:  #�ж��б�Ϊ��ʱ
            p = ''.join(p).split('LISTENING')[1].split()[0].strip()#��LISTENING���ж�������PID������TIME_WAIT��ESTABLISHED״̬
            cmd = 'taskkill /f /pid %s'%p
            os.popen(cmd)
            print 'ִ�йر�APPIUM��������ɹ���PIDΪ��%s'%p
        else:
            print 'kill APPIUM����ʧ�ܣ�����Ķ˿ں��� %s �������Ƿ�����˿��Ƿ�һ�£�'%a
