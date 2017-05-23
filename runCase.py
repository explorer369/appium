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
def doInstall(deviceids,host, port, bootstrap_port, appium_log_path):

    count = len(deviceids)               # ��ȡ�ֻ����б�ĳ��ȣ����浽count
    port_list = range(4723,4723+count)   # ���count����3����ôport_list���ֵΪ��4723,4724,4725
    bootstrap_port = range(4780,4780+count)   #���count����3����ôport_list���ֵΪ��4780,4781,4782
    for i in range(len(deviceids)):
        cmd ='start /b appium -a '+ host +' -p '+ str(port_list[i])+ ' --bootstrap-port '+ str(bootstrap_port[i]) +  ' --session-override --log '+ '"'+appium_log_path + '" --command-timeout 600'
        p = subprocess.call(cmd, shell=True,stdout=open('TestResult\\cmdlogs.log','w'),stderr=subprocess.STDOUT)
        SettingDevice.Setting_device()
        #subprocess.Popen('start /b appium -a '+ host +' -p '+ str(port_list[i])+ ' --bootstrap-port '+ str(bootstrap_port[i]) +  ' --session-override --log '+ '"'+appium_log_path + " --command-timeout 600")
        driver = webdriver.Remote('http://' + host +':'+str(port_list[i])+'/wd/hub',desired_caps)
        util.doInThread(load_tests,deviceids[i])    #�˴���� deviceids = ['0123456789ABCDEF'] d = <uiautomator.AutomatorDevice object at 0x01BE1530> installapk = <function installapk at 0x01F91D70>
        # �����ö��̷߳�ʽִ����installapk����
def start_appium(deviceids,host,appium_log_path):

    count = len(deviceids)               # ��ȡ�ֻ����б�ĳ��ȣ����浽count
    port_list = range(4723,4723+count)   # ���count����3����ôport_list���ֵΪ��4723,4724,4725
    bootstrap_port = range(4780,4780+count)   #���count����3����ôport_list���ֵΪ��4780,4781,4782
    for i in range(len(deviceids)):
        cmd ='start /b appium -a '+ host +' -p '+ str(port_list[i])+ ' --bootstrap-port '+ str(bootstrap_port[i]) +  ' --session-override --log '+ '"'+appium_log_path + '" --command-timeout 600'
        p = subprocess.call(cmd, shell=True,stdout=open('TestResult\\cmdlogs.log','w'),stderr=subprocess.STDOUT)
        print('��������http://' + host +':'+str(port_list[i])+'/wd/hub')
    time.sleep(5)   #�ȴ���������
def util_start_appium(ip):
    for i in range(len(ip)):
        subprocess.Popen('start /b appium -a '+ host +' -p '+ str(4723+2*i)+ ' --bootstrap-port '+ str(bootstrap_port) +  ' --session-override --log '+ '"'+appium_log_path + '" --command-timeout 600')
        time.sleep(3.5)
        dingwei = webdriver.Remote("http://localhost:"+str(4723+2*i)+"/wd/hub", desired_caps)
        dingwei = DingWei(wzj, name)
        t = threading.Thread(target=dingwei.begin)
        tt.append(t)
def load_tests():
    #logger�ӵ��˴�eclispe������־����ӵ�����Ҳ����
 #   logger = log.Logger('TestResult/log.log',clevel = logging.INFO,Flevel = logging.INFO)
    test_file_strings = glob.glob(r'Case\\test_*.py')
    module_strings = [str[5:len(str)-3] for str in test_file_strings]# Case\test_��¼����.py �ӵ�5����ʼȡ�������������� �����test_��¼����
    print '����ȡ������Case!'
    for Case in module_strings:
        print Case
    caseList = '\n'.join(module_strings)
    suites = [unittest.defaultTestLoader.loadTestsFromName(str) for str in module_strings]
    testSuite = unittest.TestSuite(suites)
    return testSuite
if __name__ == '__main__':
    logger = util.logger          # �����߳�LOG����
    deviceids = finddevices()
    try:
            start_appium(deviceids,'localhost',"TestResult//appium.log")
            time.sleep(5)
        #if Initialization.finddevices() == True and gettime.EffectiveTime()==True: # ����Ƿ����������ֻ�����������֤OK
            #start_appium(deviceids,'localhost',"TestResult//appium.log")
            #Initialization.start_Appium('localhost','4723','4780','TestResult//appium.log')# ����APPIUP����
            timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            filename ='TestResult\\result_'+ timestr + '.html'   #������TestResultĿ¼��
            fp =open(filename,'wb')
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'�Զ������Ա���',description=u'������ϸ')
            runner.run(load_tests())
            fp.close()
            logging.shutdown()
            Initialization.stop_Appium('http://localhost:4723/wd/hub')
            print '������ɣ�������鿴���Ա��� %s'%filename
    except Exception,e:
        f=open("Errorlog.log","wb")
        traceback.print_exc(file=f)
        f.flush()
        f.close()
        traceback.print_exc()
    cmd_1 = 'taskkill /F /IM node.exe'
    os.popen(cmd_1).readlines()
    print '����node���̳ɹ���'
    thisIsLove = raw_input('�� ENTER ���˳����ڣ�')