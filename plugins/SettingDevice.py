# coding=GBK
import os,sys,time,re,xlrd,Initialization,util,AdbTool,log,logging
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from extend import Appium_Extend   #����ͼƬ�Ա�ģ��
def Setting_device(self,automationName='Appium'):
        devicename,andriodVersion,deviceModelName = Initialization.getdevices()   #��ȡ���ӵ��ֻ���Ϣ
        print u'��ǰ���ӵĻ���SNΪ��%s\n �汾Ϊ��%s\n �ͺ�Ϊ:%s'%(devicename,andriodVersion,deviceModelName)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = automationName #UiAutomator2Ĭ��ΪAppium
        desired_caps['platformVersion'] = andriodVersion  # �����ֻ��Զ���ȡ
        desired_caps['deviceName'] = devicename           # �����ֻ��Զ���ȡ
        desired_caps['appPackage'] = 'com.wxws.myticket' # �˴��ֶ���д�������Զ���ȡ����getDevices������Ҫ��ȡ��APK·���Ϳ���52��
        desired_caps['appActivity'] = 'com.myticket.activity.WelcomeActivity'
        desired_caps['unicodeKeyboard'] = True    #���������п������������ˣ������ʱ�򲻻ᵯ�����뷨����ЩԪ�ز��ᱻ��ס
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        #self.driver.keyevent(0)
def find_toast(self,eee=None,my_elenent=None):
    ''' �ж�element�Ƿ������dom�� '''
    #�÷���find_toast(self,By.XPATH,"id")(By�����·�����CLASS_NAME,CSS_SELECTOR,ID,LINK_TEXT,NAME,PARTIAL_LINK_TEXT,TAG_NAME,XPATH)
    #�÷���find_toast(self,By.ID,"idֵ")
    try:
        element = WebDriverWait(self.driver,10,0.5).until(expected_conditions.presence_of_element_located((eee,my_elenent))) #�ж�element�Ƿ������dom��
        #element = WebDriverWait(self.driver,10,1).until(expected_conditions.visibility_of_element_located((eee,my_elenent))) #�ж�ĳ��Ԫ���Ƿ�ɼ�
        logger.info("+PASS+ �ҵ���Ӧ��toast��Ϣ��")
        return True
    except Exception,e:
        logger.war("+FAIL+ δ������Ӧ��toast��Ϣ��")
        return False
    #element = WebDriverWait(self.driver,6,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,u".//*[contains(@text,'û�п�ʹ�õ��Ż�ȯ')]")))
def duo_Setting_device():
        devicename,andriodVersion,deviceModelName = Initialization.getdevices()   #��ȡ���ӵ��ֻ���Ϣ
        print u'��ǰ���ӵĻ���SNΪ��%s\n �汾Ϊ��%s\n �ͺ�Ϊ:%s'%(devicename,andriodVersion,deviceModelName)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = andriodVersion  # �����ֻ��Զ���ȡ
        desired_caps['deviceName'] = devicename           # �����ֻ��Զ���ȡ
        desired_caps['appPackage'] = 'com.wxws.myticket' # �˴��ֶ���д�������Զ���ȡ����getDevices������Ҫ��ȡ��APK·���Ϳ���52��
        desired_caps['appActivity'] = 'com.myticket.activity.WelcomeActivity'
        desired_caps['unicodeKeyboard'] = True    #���������п������������ˣ������ʱ�򲻻ᵯ�����뷨����ЩԪ�ز��ᱻ��ס
        desired_caps['resetKeyboard'] = True
        #self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        return desired_caps

def shoushimima(self):
    view = self.driver.find_elements_by_id('com.android.keyguard:id/lockPattern')   #�Ź�����
    print view
    welem = view[0]
    startX = welem.location.get('x')    #��һ��λ�õ�x,y����90   Ԫ�ص������Ͻ��x����
    startY = welem.location.get('y')    #774                     Ԫ�ص������Ͻ��y����
    height = welem.size["height"]      #��Ԫ�صĸߺͿ�900
    width = welem.size["width"]        #900
    ystep = height / 4                  #��y���ƶ�4��֮һλ��
    xstep = width / 4                   #��x���ƶ�4��֮һλ��

    x1 = (2 * startX + width) / 2 - (width / 4)     #1��λ��
    y1 = (2 * startY + height) / 2 - (height / 4)    #1��λ��
    x2 = (2 * startX + width) / 2                   # 2��λ��
    y2 = startY + yStep                             # 2��λ��
    x3 = (2 * startX + width) / 2 + (width / 4)    #3��λ��
    y3 = (2 * startY + height) / 2 - (height / 4)    #3��λ��
    x4 = (2 * startX + width) / 2 - (width / 4)      #4��λ��
    y4 = (2 * startY + height) / 2                   #4��λ��
    x5 = (2 * startX + width) / 2                           #5��λ��
    y5 = (startY + yStep) + (height / 4)                    #5��λ��
    x6 = (2 * startX + width) / 2 + (width / 4)             #6��λ��
    y6 = (2 * startY + height) / 2                    #6��λ��
    x7 = (2 * startX + width) / 2 - (width / 4)          #7��λ��
    y7 = (2 * startY + height) / 2 + (height / 4)                       #7��λ��
    x8 = (2 * startX + width) / 2                        #8��λ��
    y8 = (startY + yStep) + (height / 4)*2                       #8��λ
    x9 = (2 * startX + width) / 2 + (width / 4)                        #9��λ��
    y9 = (2 * startY + height) / 2 + (height / 4)                       #9��λ
    TouchAction(self.driver).press(x=x1,y=y1).wait(1000).move_to(x=0,y=yStep).wait(1000).move_to(x=0,y=yStep).wait(1000).release().perform()
    TouchAction(self.driver).press(x=x2,y=y2).wait(1000).move_to(x=0,y=yStep).wait(1000).move_to(x=0,y=yStep).wait(1000).release().perform()
    TouchAction(self.driver).press(x=x3,y=y3).wait(1000).move_to(x=0,y=yStep).wait(1000).move_to(x=0,y=yStep).wait(1000).release().perform()
    TouchAction(self.driver).press(x=x4,y=y4).wait(1000).move_to(x=xStep,y=0).wait(1000).move_to(x=0,y=yStep).wait(1000).release().perform()
    TouchAction(self.driver).press(x=x5,y=y5).wait(1000).move_to(x=0,y=yStep).wait(1000).move_to(x=0,y=yStep).wait(1000).release().perform()
    TouchAction(self.driver).press(x=x6,y=y6).wait(1000).move_to(x=0,y=yStep).wait(1000).move_to(x=0,y=yStep).wait(1000).release().perform()
    TouchAction(self.driver).press(x=x7,y=y7).wait(1000).move_to(x=0,y=yStep).wait(1000).move_to(x=0,y=yStep).wait(1000).release().perform()
    TouchAction(self.driver).press(x=x8,y=y8).wait(1000).move_to(x=0,y=yStep).wait(1000).move_to(x=0,y=yStep).wait(1000).release().perform()
    TouchAction(self.driver).press(x=x9,y=y9).wait(1000).move_to(x=0,y=yStep).wait(1000).move_to(x=0,y=yStep).wait(1000).release().perform()
    #TouchAction(self.driver).press(x=228,y=647).move_to(x=228,y=647).wait(100).move_to(x=812,y=647).wait(100).move_to(x=812,y=940).wait(100).move_to(x=812,y=1241).release().perform()
    #TouchAction(self.driver).press(100,100).move_to(200,200).move_to(300,300).release().perform()
def shoushimima_my(self):
    view = self.driver.find_elements_by_id('com.android.keyguard:id/lockPattern')   #�Ź�����
    welem = view[0]
    start_x  = welem.location.get('x')
    start_y  = welem.location.get('y')
    viewHeight  = welem.size["height"]
    viewWidth  = welem.size["width"]
    Point=[]
    centerCxCy = []   #123456789�����б�
    w = viewWidth / 3
    h = viewHeight / 3
    for i in range(0,3) :
        for j in range(0,3):
            p1 = (i*w)+w/2+start_x,(j*h)+h/2+start_y
            Point.append(p1)
    for i in range(0,9,3):
        a1 = Point[i]
        centerCxCy.append(a1)
    for i in range(0,9,3):
        a1 = Point[i+1]
        centerCxCy.append(a1)
    for i in range(0,9,3):
        a1 = Point[i+2]
        centerCxCy.append(a1)
    print centerCxCy          #[(240, 924), (540, 924), (840, 924), (240, 1224), (540, 1224), (840, 1224), (240, 1524), (540, 1524), (840, 1524)]

def scroll(self,scroll='left',number=1,times=1000):
    x = self.driver.get_window_size()["width"]
    y = self.driver.get_window_size()["height"]
    top1 = x/2                  #X������ĵ�
    foot1 = y/2                #Y������ĵ�
    if scroll == 'up':
        for i in range(0,number):
            self.driver.swipe(top1,y-250,top1,20,times)#�˴�Y-250�������ϻ���ʱAPP�ײ��й̶������磺����֧����ť����
            time.sleep(1)
            logger.info("+PASS+  ���ϻ���%s�γɹ���"%(i+1))
    elif scroll == "down":
        for i in range(0,number):
            self.driver.swipe(top1,250,top1,y-20,times) #�˴���Ϊ250�������»���ʱAPP�����й̶���
            time.sleep(1)
            logger.info("+PASS+  ���»���%s�γɹ���"%(i+1))
    elif scroll == "left":
        for i in range(0,number):
            self.driver.swipe(x-20,foot1,20,foot1,times)
            time.sleep(1)
            logger.info("+PASS+  ���󻬶�%s�γɹ���"%(i+1))
    elif scroll == "right":
        for i in range(0,number):
            self.driver.swipe(20,foot1,x-20,foot1,times)
            time.sleep(1)
            logger.info("+PASS+  ���һ���%s�γɹ���"%(i+1))
def get_element_screen(self,method=None,TEXT=None,number=0,name="image"):
    '''��ȡ�ֲ�ͼƬ��Ϊԭʼ��ȷͼ�����Ա�'''
    #�÷���SettingDevice.get_element_screen(self,"id","com.wxws.myticket:id/etBecity")
    element = get_element(self,method,TEXT,number)
    self.extend.get_screenshot_by_element(element).write_to_file("D:\\screen", name)
    self.assertTrue(os.path.isfile("D:\\screen\\%s.png"%name))
    logger.info("+PASS+  ��ͼ�ɹ���������D:\\screen\\%s.png"%name)
def test_same_as(self,method=None,TEXT=None,number=0,percent=100,screen_path="D:\\screen\\image.png"):
    '''ͼƬ�Ա�,�÷���SettingDevice.test_same_as(self,"id","com.wxws.myticket:id/etBecity",percent=100) percent��ʾ100%����'''
    element = get_element(self,method,TEXT,number)
    load = self.extend.load_image(screen_path)    #��ȡ�Աȵ�ͼƬ��ԭʼͼƬ��
    #Ҫ��ٷְ����� #�Ա�ͼƬ��percentֵ��Ϊ0����100%����ʱ����True�����õ�ֵԽ�����Խ��
    result = self.extend.get_screenshot_by_element(element).same_as(load, 100-percent)   #��ȡ��ͼƬ��loadԭʼͼ�Աȣ�0��ʾ��ȫ����
    self.assertTrue(result)
logger = log.Logger('TestResult//log.log')
def get_element(self,method,TEXT,number):

    '''��ȡ�ؼ�Ԫ��'''
    if method == "name":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_name(TEXT))
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "class_name":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_class_name(TEXT))
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "css":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_css_selector(TEXT))
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "id":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_id(TEXT))
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "link":
        try:
         # TEXT = is_chinese(TEXT)
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_link_text(TEXT))
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "partial_link":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_partial_link_text(TEXT))
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "tag":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_tag_name(TEXT))
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "xpath":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_xpath(TEXT))
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "desc":  #content-desc
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_accessibility_id(TEXT))
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "class_names":
        try:
            element = self.driver.find_elements_by_class_name(TEXT)
            element = element[number]
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "elements_css":
        try:
            element = self.driver.find_elements_by_css_selector(TEXT)
            element = element[number]
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "ids":  #('ids','password','881218',0)
        try:
            element = self.driver.find_elements_by_id(TEXT)
            element = element[number]
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "links":
        try:
            element = self.driver.find_elements_by_link_text(TEXT)
            element = element[number]
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "names":
        try:
            element = self.driver.find_elements_by_name(TEXT)
            element = element[number]
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "partial_links":
        try:
            element = self.driver.find_elements_by_partial_link_text(TEXT)
            element = element[number]
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "tags":
        try:
            element = self.driver.find_elements_by_tag_name(TEXT)
            element = element[number]
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "xpaths":
        try:
            element = self.driver.find_elements_by_xpath(TEXT)
            element = element[number]
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "descs":   #content-desc
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_elements_by_accessibility_id(TEXT))
            element = element[number]
            logger.info('+PASS+  �ҵ�"%s"Ԫ��'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)

def ErrorLog(self):
    Testtime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    '''���������Ĵ���ʽ
    '''
    time.sleep(1.5)
    self.driver.get_screenshot_as_file("TestResult\\screenshot\\Failed\\%s.png"%Testtime)
    print logger.war('+FAIL+  δ�ҵ�"%s"Ԫ�أ� �ѽ�ͼ'%TEXT)
    assertverify()
def assertverify():
    #��������Ƿ����ִ�кͶ���ʧ�ܱ���ΪFAIL
    if command == 'assert':
        self.assertEqual(111,TEXT,u'δ�ҵ�:\"%s\"'%TEXT)
    elif command == 'verify':
        pass
