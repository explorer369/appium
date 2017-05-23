#coding:GBK
import logging,os,sys,time,traceback
from ConfigParser import ConfigParser
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import log    #���뱾��ģ��
reload(sys)
sys.setdefaultencoding('GBK')
global driver,Testtime
def config():
    configfile='config.txt'
    config=ConfigParser()
    config.read(configfile)
    command = config.get('AssertionMode','command')
    return command
command = config()
logger = log.Logger('TestResult//log.log', clevel = logging.DEBUG, Flevel = logging.INFO)
def find_name(self,method=None,TEXT=None,number=0,send_keys=None,get_element=None,select_keys=None,nb=None,times=None):   #�˴�˳��Ҫ�ı䣬���������ں���ӵ���Ҫ��
    Testtime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    '''�÷���self.find_name('id','com.wxws.myticket:id/rl_notification')
           self.find_name('name','���')
           self.find_name('class_name','android.widget.TextView')
           self.find_name('class_names','android.widget.TextView',1)
           self.find_name('xpath',"//android.view.View[@index='2']")
    '''
    def duoyuanshu_1():    #��ȡ��һ��Ԫ��
        if method == "name":
            try:
                emmm1 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_name(TEXT))
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "class_name":
            try:
                emmm1 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_class_name(TEXT))
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "css":
            try:
                emmm1 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_css_selector(TEXT))
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "id":
            try:
                emmm1 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_id(TEXT))
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "link":
            try:
                emmm1 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_link_text(TEXT))
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "partial_link":
            try:
                emmm1 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_partial_link_text(TEXT))
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "tag":
            try:
                emmm1 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_tag_name(TEXT))
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "xpath":
            try:
                emmm1 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_xpath(TEXT))
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "class_names":
            try:
                emmm = self.driver.find_elements_by_class_name(TEXT)
                emmm1 = emmm[number]
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "elements_css":
            try:
                emmm = self.driver.find_elements_by_css_selector(TEXT)
                emmm1 = emmm[number]
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "ids":  #('ids','password','881218',0)
            try:
                emmm = self.driver.find_elements_by_id(TEXT)
                emmm1 = emmm[number]
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "links":
            try:
                emmm = self.driver.find_elements_by_link_text(TEXT)
                emmm1 = emmm[number]
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "names":
            try:
                emmm = self.driver.find_elements_by_name(TEXT)
                emmm1 = emmm[number]
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "partial_links":
            try:
                emmm = self.driver.find_elements_by_partial_link_text(TEXT)
                emmm1 = emmm[number]
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "tags":
            try:
                emmm = self.driver.find_elements_by_tag_name(TEXT)
                emmm1 = emmm[number]
                return emmm1
            except Exception,e:
                ErrorLog(self)
        elif method == "xpaths":
            try:
                emmm = self.driver.find_elements_by_xpath(TEXT)
                emmm1 = emmm[number]
                return emmm1
            except Exception,e:
                ErrorLog(self)
    def duoyuanshu_2():    #��ȡ�ڶ���Ԫ��
        if number == "name":
            try:
                emmm2 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_name(send_keys))
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "class_name":
            try:
                emmm2 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_class_name(send_keys))
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "css":
            try:
                emmm2 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_css_selector(send_keys))
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "id":
            try:
                emmm2 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_id(send_keys))
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "link":
            try:
                emmm2 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_link_text(send_keys))
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "partial_link":
            try:
                emmm2 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_partial_link_text(send_keys))
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "tag":
            try:
                emmm2 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_tag_name(send_keys))
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "xpath":
            try:
                emmm2 = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_xpath(send_keys))
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "class_names":
            try:
                emmm = self.driver.find_elements_by_class_name(send_keys)
                emmm2 = emmm[number]
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "elements_css":
            try:
                emmm = self.driver.find_elements_by_css_selector(send_keys)
                emmm2 = emmm[number]
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "ids":  #('ids','password','881218',0)
            try:
                emmm = self.driver.find_elements_by_id(send_keys)
                emmm2 = emmm[number]
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "links":
            try:
                emmm = self.driver.find_elements_by_link_text(send_keys)
                emmm2 = emmm[number]
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "names":
            try:
                emmm = self.driver.find_elements_by_name(send_keys)
                emmm2 = emmm[number]
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "partial_links":
            try:
                emmm = self.driver.find_elements_by_partial_link_text(send_keys)
                emmm2 = emmm[number]
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "tags":
            try:
                emmm = self.driver.find_elements_by_tag_name(send_keys)
                emmm2 = emmm[number]
                return emmm2
            except Exception,e:
                ErrorLog(self)
        elif number == "xpaths":
            try:
                emmm = self.driver.find_elements_by_xpath(send_keys)
                emmm2 = emmm[number]
                return emmm2
            except Exception,e:
                ErrorLog(self)
    def assertverify():
        #��������Ƿ����ִ�кͶ���ʧ�ܱ���ΪFAIL
        if command == 'assert':
            self.assertEqual(111,TEXT,u'δ�ҵ�:\"%s\"'%TEXT)
        elif command == 'verify':
            pass
        #�˴�logger��eclipse�������־�й������ӵ�������ظ�

    def click_input(self):
        '''���ؼ�ʱ������������
        '''
        logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
        emmm.click()
        time.sleep(1.5)
        self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
        #TEXTbbb = FontColor.printRed(u'%s'.encode("gb2312")%TEXT)
        if number == 0:
            logger.info('+PASS+  ���"%s"Ԫ�سɹ����ѱ����ͼ'%TEXT)
        else:
            logger.info('+PASS+  �����%s��"%s"Ԫ�سɹ����ѱ����ͼ'%(number,TEXT))
        #time.sleep(1.5)
    def send_keysaaa(self):
        '''���������������zd
        '''
        logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
        emmm.send_keys(send_keys)
        time.sleep(1.5)
        self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
        logger.info('+PASS+  ����"%s"�ɹ����ѱ����ͼ'%send_keys)
        return send_keys
        #time.sleep(1.5)
    def ErrorLog(self):
        '''���������Ĵ���ʽ
        '''
        time.sleep(1.5)
        self.driver.get_screenshot_as_file("TestResult\\screenshot\\Failed\\%s.png"%Testtime)
        print logger.war('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
        assertverify()
        #time.sleep(1.5)
    def gettext(self):
        #��ȡԪ�ص��ı�ֵ('id',"startLogin"��get_element='text')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            abc = emmm.text
            #abc = FontColor.printRed(u"%s".encode("gb2312")%abc)
            logger.info('+PASS+  ��ȡ==="%s"===Ԫ����Ϣ�ɹ����ѷ��ؽ��'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ��ȡԪ��text��Ϣʧ�ܣ�����ÿؼ��Ƿ�֧��')
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣

    def clear_element(self):  #####
        #����������ı�ֵ('id',"startLogin"��get_element='clear')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            emmm.clear()
            logger.info('+PASS+  ��������"%s"Ԫ�����ݳɹ�'%TEXT)
            self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
        except Exception, e:
             logger.war('+FAIL+  ��������"%s"Ԫ������ʧ�ܣ���ȷ�ϴ���Ŀؼ��������'%TEXT)
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    def get_location(self):
        #��ȡԪ������('id',"startLogin"��get_element='location')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            abc = emmm.location
            x = emmm.location.get('x')
            y = emmm.location.get('y')
            logger.info('+PASS+  ��ȡ==="%s"===Ԫ������ֵ�ɹ����ѷ��ؽ��'%abc)
            logger.info('+PASS+  �����ص�X����Ϊ"%s" Y����Ϊ"%s"���ѷ��ؽ��(Ԫ������,X,Y)'%(x,y))
            return abc,x,y
        except Exception, e:
             logger.war('+FAIL+  ��ȡ"%s"Ԫ������ֵʧ�ܣ����鴫��Ŀؼ��Ƿ���ȷ'%TEXT)
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    def get_rect(self):
        #��ȡԪ�صĴ�С��λ�õ��ֵ�('id',"startLogin"��get_element='rect')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            abc = emmm.rect
            logger.info('+PASS+  ֵΪ==="%s"===Ԫ�صĴ�С��λ�õ��ֵ�ɹ����ѷ��ؽ��'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ��ȡ"%s"Ԫ�صĴ�С��λ�õ��ֵ�ʧ��'%TEXT)
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    def get_submit(self):
        #�ύ��('id',"startLogin"��get_element='submit')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            emmm.submit()
            self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  �ύ�����ݳɹ����ѽ�ͼ���ύ��Ԫ��Ϊ"%s"'%TEXT)
        except Exception, e:
            logger.war('+FAIL+  �ύ������ʧ�ܣ������Ԫ���Ƿ�֧�ֱ��ύ���ѽ�ͼ��Ҫ�ύ��Ԫ��Ϊ"%s"'%TEXT)
            raise Exception()   #�ֶ������쳣���ô˴����׳��쳣

    def my_get_attribute(self):
        #��ȡԪ�ص�����ֵ('id',"startLogin"��get_element='get_attribute')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            abc = emmm.get_attribute(TEXT)
            logger.info('+PASS+  ��ȡԪ������ֵ�ɹ�,����ֵΪ==="%s"===���ѷ��ؽ����'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ��ȡ"%s"Ԫ������ֵʧ�ܣ����鴫���Ԫ����ȷ��'%TEXT)
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣


    def my_context_click(self):
        #�һ�Ԫ��('id',"startLogin"��get_element='context_click')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            ActionChains(self.driver).context_click(emmm).perform()
            self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  �һ���Ԫ�سɹ���')
        except Exception, e:
            logger.war('+FAIL+  �һ���Ԫ��ʧ�ܣ���ȷ�ϸ�Ԫ�ؿɱ��һ���')
            raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    def my_double_click(self):
        #˫��Ԫ��('id',"startLogin"��get_element='double_click')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            ActionChains(self.driver).double_click(emmm).perform()
            self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  ˫����Ԫ�سɹ���')
        except Exception, e:
            logger.war('+FAIL+  ˫����Ԫ��ʧ�ܣ���ȷ�ϸ�Ԫ�ؿɱ�˫����')
            raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    def my_move_to_element(self):
        #�����ͣ��һ��Ԫ����('id',"startLogin"��get_element='move_to_element')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            ActionChains(self.driver).move_to_element(emmm).perform()
            logger.info('+PASS+  �����ͣ�ڸ�Ԫ���ϳɹ���')
        except Exception, e:
             logger.war('+FAIL+  �����ͣ�ڸ�Ԫ����ʧ�ܣ���ȷ�ϸ�Ԫ���Ƿ�֧�֣�')
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    def select_down(self):
        #ѡ���������������('id',"startLogin"��get_element='select',number=1)
        #('id',"startLogin"��get_element='select',select_keys=u'����')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            if select_keys == None:
                Select(emmm).select_by_index(number)
                self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
                logger.info('+PASS+  ѡ���"%s"��Ԫ�سɹ���(��0��ʼ����)'%number)
            else:
                Select(emmm).select_by_visible_text(select_keys)
                self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
                logger.info('+PASS+  ѡ��"%s"�ɹ���'%select_keys)
        except Exception, e:
             logger.war('+FAIL+  ִ��ѡ��Ԫ��ʧ�ܣ���ȷ�ϸ�Ԫ��֧������ѡ��')
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    # �ص�����
    def scroll_top(self):
        #self.func(get_element='scroll_top')
        try:
            if self.driver.name == "chrome":
                js = "var q=document.body.scrollTop=0"
            else:
                js = "var q=document.documentElement.scrollTop=0"
            return self.driver.execute_script(js)
        except Exception, e:
             logger.war('+FAIL+  ִ�лص�����ʧ�ܣ�')
             #raise Exception()   #�ֶ������쳣���ô˴����׳��쳣��ע�ͺ�ִ��ʧ��Ҳ����ִ�к����
    # �����ײ�
    def scroll_foot(self):
        #self.func(get_element='scroll_foot')
        try:
            if self.driver.name == "chrome":
                js = "var q=document.body.scrollTop=10000"
            else:
                js = "var q=document.documentElement.scrollTop=10000"
            return self.driver.execute_script(js)
        except Exception,e:
            logger.war('+FAIL+  ִ�������ײ�ʧ�ܣ�')
            #raise Exception()   #�ֶ������쳣���ô˴����׳��쳣��ע�ͺ�ִ��ʧ��Ҳ����ִ�к����
    def scroll_element(self):
        #�ƶ���Ԫ��element����ġ����ˡ��뵱ǰ���ڵġ�����������
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", emmm)
            logger.info('+PASS+ Ԫ�ض���ġ����ˡ��뵱ǰ���ڵġ�����������ɹ���"%s"'%TEXT)
        except Exception,e:
            logger.war('+FAIL+ Ԫ�ض���ġ����ˡ��뵱ǰ���ڵġ�����������ʧ�ܣ�"%s"'%TEXT)
    def scroll_element_foot(self):
        #�ƶ���Ԫ��element����ġ��׶ˡ��뵱ǰ���ڵġ��ײ�������
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            self.driver.execute_script("arguments[0].scrollIntoView(false);", emmm)
            logger.info('+PASS+ Ԫ�ض���ġ��׶ˡ��뵱ǰ���ڵġ��ײ�������ɹ���"%s"'%TEXT)
        except Exception,e:
            logger.war('+FAIL+ Ԫ�ض���ġ��׶ˡ��뵱ǰ���ڵġ��ײ�������ʧ�ܣ�"%s"'%TEXT)
    def click_scroll_element(self):
        #���Ԫ���»�һ��('id',"startLogin",number=0,get_element='click_scroll_element')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            for i in range(0,number):
                emmm.send_keys(Keys.DOWN)
                time.sleep(0.3)#�Ӳ��Ӷ�û�����⣬��Ϊ����������ܵȴ�
                logger.info('+PASS+ ���Ԫ���»��ɹ���������%s��'%number)
        except Exception,e:
            logger.war('+FAIL+ ��Ԫ��"%s"�»�ʧ�ܣ�'%TEXT)
            traceback.print_exc()

    #��������Ϊ��Ԫ��ʱ����֧ʽ
    def select_down_s(self):
        #ѡ���Ԫ���������������('ids',"startLogin"��get_element='select',number=1,nb=1)
        #('ids',"startLogin"��get_element='select',number=0,select_keys=u'����')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            if select_keys == None:
                Select(emmm).select_by_index(nb)
                self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
                logger.info('+PASS+  ѡ���"%s"��Ԫ�سɹ���(��0��ʼ����)'%nb)
            else:
                Select(emmm).select_by_visible_text(select_keys)
                self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
                logger.info('+PASS+  ѡ��"%s"�ɹ���'%select_keys)
        except Exception, e:
             logger.war('+FAIL+  ִ��ѡ��Ԫ��ʧ�ܣ���ȷ�ϸ�Ԫ��֧������ѡ��')
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    def click_scroll_elements(self):
        #���Ԫ���»�һ��('ids',"startLogin"��get_element='click_scroll_element',number=1,nb=1)
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            for i in range(0,nb):
                emmm.send_keys(Keys.DOWN)
                time.sleep(0.3)#�Ӳ��Ӷ�û�����⣬��Ϊ����������ܵȴ�
                logger.info('+PASS+ ���Ԫ���»��ɹ���������%s��'%nb)
        except Exception,e:
            logger.war('+FAIL+ ��Ԫ��"%s"�»�ʧ�ܣ�'%TEXT)
            traceback.print_exc()
    def removeAttr_readonly_sendkeys(self):
        #ȥ��ֻ�����Բ���ֵ('css',"input[name='outBusStartTime']"��get_element='readonly',send_keys='2016-12-14')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            js="$(\"%s\").removeAttr('readonly');$(\"%s\").attr('value','%s')%(TEXT,TEXT,send_keys)"
            self.driver.execute_script(js)
            logger.info('+PASS+ ȥ��Ԫ�����Գɹ���')
        except Exception,e:
            logger.war('+FAIL+ ȥ��Ԫ������ʧ�ܣ�')
            traceback.print_exc()
    def removeAttr_readonly(self):
        #ȥ��ֻ������('css',"input[name='outBusStartTime']"��get_element='readonly')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            self.driver.execute_script("$(\"%s\").removeAttr('readonly')"%TEXT)
            logger.info('+PASS+ ȥ��Ԫ�����Գɹ���')
        except Exception,e:
            logger.war('+FAIL+ ȥ��Ԫ������ʧ�ܣ�')
            traceback.print_exc()

    def removeAttr_send_keys(self):
        #ȥ��ֻ�����Բ���ֵ('css',"input[name='outBusStartTime']"��get_element='readonly',send_keys='2016-12-12')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            self.driver.execute_script("$(\"%s\").removeAttr('readonly');$(\"%s\").attr('value',\"%s\")"%(TEXT,TEXT,send_keys))
            logger.info('+PASS+ ȥ��Ԫ�����Գɹ���')
        except Exception,e:
            logger.war('+FAIL+ ȥ��"%s"Ԫ������ʧ��')
            traceback.print_exc()


    def my_pinch(self):
        #��Ԫ����ִ��ģ��˫ָ����С��������'id',"dfas",get_element="pinch"��
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            self.driver.pinch(emmm)
            logger.info('+PASS+ ��Ԫ����ִ��ģ��˫ָ��ɹ���')
        except Exception,e:
            logger.war('+FAIL+ ��Ԫ����ִ��ģ��˫ָ��ʧ�ܣ�')
            traceback.print_exc()
    def my_zoom(self):
        #��Ԫ����ִ�зŴ������'id',"dfas",get_element="zoom"��
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            self.driver.zoom(emmm)
            logger.info('+PASS+ ��Ԫ����ִ�зŴ�����ɹ���')
        except Exception,e:
            logger.war('+FAIL+ ��Ԫ����ִ�зŴ����ʧ�ܣ�')
            traceback.print_exc()
    def my_tagName(self):
        #����Ԫ�ص�tagName('id',"startLogin"��get_element='tagname')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            abc = emmm.tag_name()
            logger.info('+PASS+  ��Ԫ�ص�tagname��==="%s"===�����ѷ��ؽ����'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  �����"%s"Ԫ�ض���û�����Եı�ǩ�����봫����ȷ��Ԫ�أ�'%TEXT)
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    def my_is_selected(self):
        #�ж�Ԫ���Ƿ�ѡ��('id',"startLogin"��get_element='is_selected')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            abc = emmm.is_selected()
            if abc == True:
                logger.info('+PASS+  "%s"��==="%s"===ѡ��״̬�����ѷ��ؽ������True��'%TEXT)
            else:
                logger.info('+PASS+  "%s"��==="%s"===δѡ��״̬�����ѷ��ؽ������False��'%TEXT)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ����"%s"Ԫ��ִ��ʧ�ܣ����鴫���Ԫ����ȷ��'%TEXT)
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    def my_is_enabled(self):
        #�ж�Ԫ���Ƿ�ʹ��('id',"startLogin"��get_element='is_enabled')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            abc = emmm.is_enabled()
            if abc == True:
                logger.info('+PASS+  ��Ԫ����==="%s"===��ʹ��״̬�����ѷ��ؽ������True��'%TEXT)
            else:
                logger.info('+PASS+  ��Ԫ��==="%s"===���Ǳ�ʹ��״̬�����ѷ��ؽ������False��'%TEXT)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ����"%s"Ԫ��ִ��ʧ�ܣ����鴫���Ԫ����ȷ��'%TEXT)
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    def my_is_displayed(self):
        #�ж�Ԫ���Ƿ���ʾ('id',"startLogin"��get_element='is_displayed')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            abc = emmm.is_displayed()
            if abc == True:
                logger.info('+PASS+  ��Ԫ��==="%s"===�ǿɼ�״̬�����ѷ��ؽ������True��'%TEXT)
            else:
                logger.info('+PASS+  ��Ԫ��==="%s"===�ǲ��ɼ�״̬�����ѷ��ؽ������False��'%TEXT)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ����"%s"Ԫ��ִ��ʧ�ܣ����鴫���Ԫ����ȷ��'%TEXT)
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    def my_size(self):
        #����Ԫ�صĴ�С('id',"startLogin"��get_element='size')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            abc = emmm.size
            logger.info('+PASS+  ��Ԫ�صĴ�СΪ==="%s"===�����ѷ��ؽ����'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ����"%s"Ԫ��ִ��ʧ�ܣ����鴫���Ԫ����ȷ��'%TEXT)
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    def css_name(self):
        #��ȡCSS������ֵ('id',"startLogin"��get_element='css')
        try:
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            abc = emmm.value_of_css_property(TEXT)
            logger.info('+PASS+  ��ȡCSSԪ������ֵ�ɹ���������Ϊ==="%s"===�ѷ��ؽ��'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ��ȡ"%s"Ԫ������ֵʧ�ܣ��㴫�����css_name��'%TEXT)
             raise Exception()   #�ֶ������쳣���ô˴����׳��쳣
    def panduanfangfa(self):   #��Ԫ��ʱ
            if send_keys == None and get_element == None:
                click_input(self)
            elif send_keys != None and get_element == None:
                return send_keysaaa(self)
            elif get_element == 'text':
                return gettext(self)                     #��ȡԪ�ص��ı�ֵ
            elif get_element == 'clear':
                clear_element(self)
            elif get_element == 'location':
                return get_location(self)                #��ȡԪ������
            elif get_element == 'submit':
                get_submit(self)
            elif get_element == 'css':
                return css_name(self)                    #��ȡCSS������ֵ
            elif get_element == 'get_attribute':
                return my_get_attribute(self)            #��ȡԪ�ص�����ֵ
            elif get_element == 'is_selected':
                return my_is_selected(self)              #�ж�Ԫ���Ƿ�ѡ��
            elif get_element == 'size':
                return my_size(self)                     #����Ԫ�صĴ�С
            elif get_element == 'is_displayed':
                return my_is_displayed(self)             #�ж�Ԫ���Ƿ���ʾ
            elif get_element == 'is_enabled':
                return my_is_enabled(self)               #�ж�Ԫ���Ƿ�ʹ��
            elif get_element == 'tagname':
                return my_tagName(self)                  #����Ԫ�ص�tagname
            elif get_element == 'context_click':
                my_context_click(self)                   #�һ�Ԫ��
            elif get_element == 'double_click':
                my_double_click(self)                    #˫��Ԫ��
            elif get_element == 'move_to_element':
                my_move_to_element(self)                 #�����ͣ��һ��Ԫ����
            elif get_element == 'select':
                select_down(self)                       #ѡ���������������
            elif get_element == "scroll_top":
                scroll_top(self)                        #����������
            elif get_element == "scroll_foot":
                scroll_foot(self)                       #�������ײ�
            elif get_element == "scroll_element":
                scroll_element(self)                    #�ƶ���Ԫ��element����ġ����ˡ��뵱ǰ���ڵġ�����������
            elif get_element == "scroll_element_foot":
                scroll_element_foot(self)               #�ƶ���Ԫ��element����ġ��׶ˡ��뵱ǰ���ڵġ��ײ�������
            elif get_element == "click_scroll_element" and number !=0 :   #���Ԫ���»�һ��
                click_scroll_element(self)
            elif get_element == 'select' and nb != None:
                select_down_s(self)  #ѡ��ؼ�number��ѡ�ڼ���nb                 #ѡ���Ԫ���������������
            elif get_element == 'click_scroll_element' and nb != None:
                click_scroll_elements(self)   #ѡ��ؼ�number��ѡ�ڼ���nb       #���Ԫ���»�һ��
            elif get_element == 'readonly' and send_keys == None:
                removeAttr_readonly(self)                          #ȥ��ֻ������
            elif get_element == 'readonly' and send_keys != None:  #ȥ�������Բ���ֵ
                removeAttr_send_keys(self)
            elif get_element == "pinch":
                my_pinch(self)
            elif get_element == "zoom":
                my_zoom(self)
            elif get_element == "rect":   #��ȡԪ�ش�С��λ�õ��ֵ�
                get_rect(self)
    def my_contexts(self):
        #���ص�ǰ�Ự�е������ģ�ʹ�ú����ʶH5ҳ��Ŀؼ�(get_element='contexts')
        try:
            abc = self.driver.contexts
            logger.info('+PASS+  ��ȡ==="%s"===��ǰ�Ự�е������ĳɹ����ѷ��ؽ��'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ��ȡ��ǰ�Ự�е�������ʧ��')
             raise Exception()
    def my_current_context(self):
        #���ص�ǰ�Ự�е������ģ�ʹ�ú����ʶH5ҳ��Ŀؼ�(get_element='current_context')
        try:
            abc = self.driver.current_context
            logger.info('+PASS+  ��ȡ==="%s"===��ǰ�Ự�е������ĳɹ����ѷ��ؽ��'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ��ȡ��ǰ�Ự�е�������ʧ��')
             raise Exception()
    def my_reset(self):
        #����Ӧ�ã�����ɾ��Ӧ�����ݣ�(get_element='reset')
        try:
            self.driver.reset()
            logger.info('+PASS+  ִ������Ӧ�ò����ɹ���')
        except Exception, e:
             logger.war('+FAIL+  ִ������Ӧ�ò���ʧ�ܣ�')
             raise Exception()
    def my_hide_keyboard(self):
        #���ؼ��̣�IOSʹ��key_name���أ���׿��ʹ�ò�����(get_element='hide_keyboard')
        try:
            self.driver.hide_keyboard()
            logger.info('+PASS+  ִ�����ؼ��̳ɹ���')
        except Exception, e:
             logger.war('+FAIL+  ִ�����ؼ���ʧ�ܣ�')
             raise Exception()
    def my_current_activity(self):
        #���ص�ǰ�Ự�е������ģ�ʹ�ú����ʶH5ҳ��Ŀؼ�(get_element='current_activity')
        try:
            abc = self.driver.current_activity()
            logger.info('+PASS+  ��ȡ==="%s"===��ǰactivity�ɹ����ѷ��ؽ��'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ��ȡ��ǰ��activityʧ�ܣ�')
             raise Exception()
    def my_shake(self):
        #ҡһҡ�ֻ�(get_element='shake')
        try:
            self.driver.shake()
            logger.info('+PASS+  ҡһҡ�ֻ��ɹ���')
        except Exception, e:
             logger.war('+FAIL+  ҡһҡ�ֻ�ʧ�ܣ�')
             raise Exception()
    def my_open_notifications(self):
        #��ϵͳ֪ͨ��(get_element='open_notifications')
        try:
            self.driver.open_notifications()
            logger.info('+PASS+  ��ϵͳ֪ͨ���ɹ���')
        except Exception, e:
             logger.war('+FAIL+  ��ϵͳ֪ͨ��ʧ�ܣ�')
             raise Exception()
    def my_network_connection(self):
        #��������������ֵ(get_element='network_connection')
        try:
            abc = self.driver.network_connection
            logger.info('+PASS+  ��ȡ==="%s"===����������ֵ�ɹ����ѷ��ؽ��'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ��������������ֵʧ�ܣ�')
             raise Exception()
    def my_available_ime_engines(self):
        #���ذ�׿�豸���õ����뷨(get_element='available_ime_engines')
        try:
            abc = self.driver.available_ime_engines
            logger.info('+PASS+  ��ȡ==="%s"===��׿���õ����뷨�ɹ����ѷ��ؽ��'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ��ȡ��׿���õ����뷨ʧ�ܣ�')
             raise Exception()
    def my_is_ime_active(self):
        #��鰲׿�豸�Ƿ����뷨����(get_element='is_ime_active')
        try:
            abc = self.driver.is_ime_active()
            logger.info('+PASS+  ��ȡ==="%s"===��׿�豸�Ƿ������뷨�����ɹ����ѷ��ؽ��'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ��ȡ��׿�豸�Ƿ������뷨����ʧ�ܣ�')
             raise Exception()
    def my_deactivate_ime_engine(self):
        #�رհ�׿��ǰ�����뷨(get_element='deactivate_ime_engine')
        try:
            self.driver.deactivate_ime_engine()
            logger.info('+PASS+  �رհ�׿��ǰ�����뷨�ɹ���')
        except Exception, e:
             logger.war('+FAIL+  �رհ�׿��ǰ�����뷨ʧ�ܣ�')
             raise Exception()
    def my_active_ime_engine(self):
        #���ص�ǰ���뷨�İ���(get_element='active_ime_engine')
        try:
            abc = self.driver.active_ime_engine
            logger.info('+PASS+  ��ȡ==="%s"===���ص�ǰ���뷨�İ����ɹ����ѷ��ؽ��'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ���ص�ǰ���뷨�İ���ʧ�ܣ�')
             raise Exception()
    def my_current_url(self):
        #��ȡ��ǰҳ�����ַ(get_element='current_url')
        try:
            abc = self.driver.current_url
            logger.info('+PASS+  ��ǰҳ�����ַΪ:%s'%abc)
        except Exception, e:
             logger.war('+FAIL+  ��ȡ��ǰҳ�����ַʧ�ܣ�')
             raise Exception()
    def my_page_source(self):
        #���ص�ǰҳ���Դ(get_element='page_source')
        try:
            abc = self.driver.page_source
            logger.info('+PASS+  ��ȡ==="%s"===���ص�ǰҳ���Դ�ɹ����ѷ��ؽ��'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  ���ص�ǰҳ���Դʧ�ܣ�')
             raise Exception()
    def my_scroll(self,emmm1,emmm2):
        #��Ԫ��1������Ŀ��Ԫ��2("id","com.wxws.myticket:id/tv_ticket_cjkx","id","com.wxws.myticket:id/etBecity",get_element='scroll')
        try:
            self.driver.scroll(emmm1,emmm2)
            logger.info('+PASS+  ��Ԫ��1������Ԫ��2�ɹ���')
        except Exception, e:
             print e
             logger.war('+FAIL+  ��Ԫ��1������Ԫ��2ʧ�ܣ�')
             raise Exception()
    def my_drag_and_drop(self,emmm1,emmm2):
        #��Ԫ��1�϶���Ԫ��2(get_element='drag_and_drop')
        try:
            self.driver.drag_and_drop(emmm1,emmm2)
            logger.info('+PASS+  ��Ԫ��1�϶���Ԫ��2�ɹ���')
        except Exception, e:
             logger.war('+FAIL+  ��Ԫ��1�϶���Ԫ��2ʧ�ܣ�')
             raise Exception()
    def my_swipe(self):
        #��A�㻬����B�㣬����ʱ��Ϊ����('1000','1000','20','1000',times=500,get_element='swipe',nb=4)
        try:
            if nb == None:   #���δ����nb����ʱ����һ��Ĭ��ֵ
                self.driver.swipe(method,TEXT,number,send_keys,times)
                logger.info('+PASS+  ������1����������2�ɹ���')
            else:
                for i in range(0,nb):
                    self.driver.swipe(method,TEXT,number,send_keys,times)
                    logger.info('+PASS+  ������1����������2�ɹ���')
                    time.sleep(1)    #ÿ����һ����ͣ1S���������ܲ���ֻ���ͬһҳ����
        except Exception, e:
             logger.war('+FAIL+  ������1����������2ʧ�ܣ�')
             raise Exception()
    def my_flick(self):
        #��סA��������ٻ�����B�����('1000','1000','20','1000',get_element='flick')
        try:
            self.driver.flick(method,TEXT,number,send_keys)
            logger.info('+PASS+  ������A����ٻ���������B��ɹ���')
        except Exception, e:
             logger.war('+FAIL+  ������A����ٻ���������B��ʧ�ܣ�')
             raise Exception()
    def my_set_location(self):
        #�����豸�ľ�γ��('1000','1000','20',get_element='set_location')
        try:
            self.driver.set_location(method,TEXT,number)
            logger.info('+PASS+  �����豸�ľ�γ�ȳɹ�(%s,%s,%s)��'%(method,TEXT,number))
        except Exception, e:
             logger.war('+FAIL+  �����豸�ľ�γ��ʧ�ܣ�')
             raise Exception()
    def my_toggle_location_services(self):
        #�򿪰�׿�豸�ϵ�λ�ö�λ����(get_element='toggle_location_services')
        try:
            self.driver.toggle_location_services()
            logger.info('+PASS+  �򿪰�׿�豸�ϵ�λ�ö�λ���óɹ���')
        except Exception, e:
             print e
             logger.war('+FAIL+  �򿪰�׿�豸�ϵ�λ�ö�λ����ʧ�ܣ�')
             #raise Exception()     #��ʧ����Ҳ����ִ��
    def NOpanduanfangfa(self):   #����Ԫ��ʱ
            if get_element == "contexts":
                return my_contexts(self)            #���ص����б�
            elif get_element == "current_context":
                return my_current_context(self)    #���ص����ַ���
            elif get_element == "reset":
                my_reset(self)
            elif get_element == "hide_keyboard":
                my_hide_keyboard(self)
            elif get_element == "current_activity":
                my_current_activity(self)
            elif get_element == "shake":
                my_shake(self)
            elif get_element == "open_notifications":
                my_open_notifications(self)
            elif get_element == "network_connection":
                return my_network_connection(self)
            elif get_element == "available_ime_engines":
                return my_available_ime_engines(self)
            elif get_element == "is_ime_active":
                return my_is_ime_active(self)
            elif get_element == "deactivate_ime_engine":
                my_deactivate_ime_engine(self)
            elif get_element == "active_ime_engine":   #���ص�ǰ���뷨�İ���
                return my_active_ime_engine(self)
            elif get_element == "current_url":     #��ȡ��ǰҳ�����ַ
                return my_current_url(self)
            elif get_element == "page_source":    #��ȡ��ǰҳ���Դ
                return my_page_source(self)
    #������Ԫ��ʱ�ķ���
    if get_element == 'scroll':
        emmm1 = duoyuanshu_1()
        emmm2 = duoyuanshu_2()
        my_scroll(self,emmm1,emmm2)          #��Ԫ��1������Ԫ��2
    elif get_element == 'drag_and_drop':
        emmm1 = duoyuanshu_1()
        emmm2 = duoyuanshu_2()
        my_drag_and_drop(self,emmm1,emmm2)  #��Ԫ��origin_el�ϵ�Ŀ��Ԫ��destination_el
    elif get_element == "swipe":
        my_swipe(self)                      #��A�㻬����B��
    elif get_element == "flick":
        my_flick(self)                      #��סA�����ٻ�����B��
    elif get_element == "set_location":
        my_set_location(self)               #�����豸�ľ�γ��
    elif get_element == "toggle_location_services":
        my_toggle_location_services(self)      #�򿪰�׿�豸�ϵ�λ�ö�λ����




    elif method == "name":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_name(TEXT))
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "class_name":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_class_name(TEXT))
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "css":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_css_selector(TEXT))
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "id":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_id(TEXT))
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "link":
        try:
           # TEXT = is_chinese(TEXT)
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_link_text(TEXT))
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "partial_link":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_partial_link_text(TEXT))
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "tag":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_tag_name(TEXT))
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "xpath":
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_xpath(TEXT))
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "desc":  #content-desc
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_accessibility_id(TEXT))
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "class_names":
        try:
            emmm = self.driver.find_elements_by_class_name(TEXT)
            emmm = emmm[number]
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "elements_css":
        try:
            emmm = self.driver.find_elements_by_css_selector(TEXT)
            emmm = emmm[number]
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "ids":  #('ids','password','881218',0)
        try:
            emmm = self.driver.find_elements_by_id(TEXT)
            emmm = emmm[number]
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "links":
        try:
            emmm = self.driver.find_elements_by_link_text(TEXT)
            emmm = emmm[number]
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "names":
        try:
            emmm = self.driver.find_elements_by_name(TEXT)
            emmm = emmm[number]
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "partial_links":
        try:
            emmm = self.driver.find_elements_by_partial_link_text(TEXT)
            emmm = emmm[number]
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "tags":
        try:
            emmm = self.driver.find_elements_by_tag_name(TEXT)
            emmm = emmm[number]
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "xpaths":
        try:
            emmm = self.driver.find_elements_by_xpath(TEXT)
            emmm = emmm[number]
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif method == "descs":   #content-desc
        try:
            emmm = WebDriverWait(self.driver,10).until(lambda x: x.find_elements_by_accessibility_id(TEXT))
            emmm = emmm[number]
            return panduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    elif get_element != None:    #get_element��ֵʱִ�в���Ԫ�صķ���
        try:
            return NOpanduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    else:
        raise Exception('������Ŀؼ��������������飡')
