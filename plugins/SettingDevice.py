# coding=GBK
import os,sys,time,re,xlrd,Initialization,util,AdbTool,log,logging
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from extend import Appium_Extend   #导入图片对比模块
def Setting_device(self,automationName='Appium'):
        devicename,andriodVersion,deviceModelName = Initialization.getdevices()   #获取连接的手机信息
        print u'当前连接的机器SN为：%s\n 版本为：%s\n 型号为:%s'%(devicename,andriodVersion,deviceModelName)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = automationName #UiAutomator2默认为Appium
        desired_caps['platformVersion'] = andriodVersion  # 连上手机自动获取
        desired_caps['deviceName'] = devicename           # 连上手机自动获取
        desired_caps['appPackage'] = 'com.wxws.myticket' # 此处手动填写，如想自动获取请在getDevices下设置要获取的APK路径和开启52行
        desired_caps['appActivity'] = 'com.myticket.activity.WelcomeActivity'
        desired_caps['unicodeKeyboard'] = True    #加上这两行可以输入中文了，输入的时候不会弹出输入法，有些元素不会被盖住
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        #self.driver.keyevent(0)
def find_toast(self,eee=None,my_elenent=None):
    ''' 判断element是否出现在dom树 '''
    #用法：find_toast(self,By.XPATH,"id")(By有以下方法：CLASS_NAME,CSS_SELECTOR,ID,LINK_TEXT,NAME,PARTIAL_LINK_TEXT,TAG_NAME,XPATH)
    #用法：find_toast(self,By.ID,"id值")
    try:
        element = WebDriverWait(self.driver,10,0.5).until(expected_conditions.presence_of_element_located((eee,my_elenent))) #判断element是否出现在dom树
        #element = WebDriverWait(self.driver,10,1).until(expected_conditions.visibility_of_element_located((eee,my_elenent))) #判断某个元素是否可见
        logger.info("+PASS+ 找到相应的toast信息！")
        return True
    except Exception,e:
        logger.war("+FAIL+ 未出现相应的toast信息！")
        return False
    #element = WebDriverWait(self.driver,6,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,u".//*[contains(@text,'没有可使用的优惠券')]")))
def duo_Setting_device():
        devicename,andriodVersion,deviceModelName = Initialization.getdevices()   #获取连接的手机信息
        print u'当前连接的机器SN为：%s\n 版本为：%s\n 型号为:%s'%(devicename,andriodVersion,deviceModelName)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = andriodVersion  # 连上手机自动获取
        desired_caps['deviceName'] = devicename           # 连上手机自动获取
        desired_caps['appPackage'] = 'com.wxws.myticket' # 此处手动填写，如想自动获取请在getDevices下设置要获取的APK路径和开启52行
        desired_caps['appActivity'] = 'com.myticket.activity.WelcomeActivity'
        desired_caps['unicodeKeyboard'] = True    #加上这两行可以输入中文了，输入的时候不会弹出输入法，有些元素不会被盖住
        desired_caps['resetKeyboard'] = True
        #self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        return desired_caps

def shoushimima(self):
    view = self.driver.find_elements_by_id('com.android.keyguard:id/lockPattern')   #九宫格大框
    print view
    welem = view[0]
    startX = welem.location.get('x')    #第一个位置的x,y坐标90   元素的最左上解的x坐标
    startY = welem.location.get('y')    #774                     元素的最左上解的y坐标
    height = welem.size["height"]      #此元素的高和宽900
    width = welem.size["width"]        #900
    ystep = height / 4                  #向y轴移动4分之一位置
    xstep = width / 4                   #向x轴移动4分之一位置

    x1 = (2 * startX + width) / 2 - (width / 4)     #1的位置
    y1 = (2 * startY + height) / 2 - (height / 4)    #1的位置
    x2 = (2 * startX + width) / 2                   # 2的位置
    y2 = startY + yStep                             # 2的位置
    x3 = (2 * startX + width) / 2 + (width / 4)    #3的位置
    y3 = (2 * startY + height) / 2 - (height / 4)    #3的位置
    x4 = (2 * startX + width) / 2 - (width / 4)      #4的位置
    y4 = (2 * startY + height) / 2                   #4的位置
    x5 = (2 * startX + width) / 2                           #5的位置
    y5 = (startY + yStep) + (height / 4)                    #5的位置
    x6 = (2 * startX + width) / 2 + (width / 4)             #6的位置
    y6 = (2 * startY + height) / 2                    #6的位置
    x7 = (2 * startX + width) / 2 - (width / 4)          #7的位置
    y7 = (2 * startY + height) / 2 + (height / 4)                       #7的位置
    x8 = (2 * startX + width) / 2                        #8的位置
    y8 = (startY + yStep) + (height / 4)*2                       #8的位
    x9 = (2 * startX + width) / 2 + (width / 4)                        #9的位置
    y9 = (2 * startY + height) / 2 + (height / 4)                       #9的位
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
    view = self.driver.find_elements_by_id('com.android.keyguard:id/lockPattern')   #九宫格大框
    welem = view[0]
    start_x  = welem.location.get('x')
    start_y  = welem.location.get('y')
    viewHeight  = welem.size["height"]
    viewWidth  = welem.size["width"]
    Point=[]
    centerCxCy = []   #123456789坐标列表
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
    top1 = x/2                  #X轴的中心点
    foot1 = y/2                #Y轴的中心点
    if scroll == 'up':
        for i in range(0,number):
            self.driver.swipe(top1,y-250,top1,20,times)#此处Y-250避免向上华东时APP底部有固定条（如：立即支付按钮条）
            time.sleep(1)
            logger.info("+PASS+  向上滑动%s次成功！"%(i+1))
    elif scroll == "down":
        for i in range(0,number):
            self.driver.swipe(top1,250,top1,y-20,times) #此处设为250避免向下华东时APP顶部有固定条
            time.sleep(1)
            logger.info("+PASS+  向下滑动%s次成功！"%(i+1))
    elif scroll == "left":
        for i in range(0,number):
            self.driver.swipe(x-20,foot1,20,foot1,times)
            time.sleep(1)
            logger.info("+PASS+  向左滑动%s次成功！"%(i+1))
    elif scroll == "right":
        for i in range(0,number):
            self.driver.swipe(20,foot1,x-20,foot1,times)
            time.sleep(1)
            logger.info("+PASS+  向右滑动%s次成功！"%(i+1))
def get_element_screen(self,method=None,TEXT=None,number=0,name="image"):
    '''截取局部图片作为原始正确图用来对比'''
    #用法：SettingDevice.get_element_screen(self,"id","com.wxws.myticket:id/etBecity")
    element = get_element(self,method,TEXT,number)
    self.extend.get_screenshot_by_element(element).write_to_file("D:\\screen", name)
    self.assertTrue(os.path.isfile("D:\\screen\\%s.png"%name))
    logger.info("+PASS+  截图成功！保存在D:\\screen\\%s.png"%name)
def test_same_as(self,method=None,TEXT=None,number=0,percent=100,screen_path="D:\\screen\\image.png"):
    '''图片对比,用法：SettingDevice.test_same_as(self,"id","com.wxws.myticket:id/etBecity",percent=100) percent表示100%相似'''
    element = get_element(self,method,TEXT,number)
    load = self.extend.load_image(screen_path)    #获取对比的图片（原始图片）
    #要求百分百相似 #对比图片，percent值设为0，则100%相似时返回True，设置的值越大，相差越大
    result = self.extend.get_screenshot_by_element(element).same_as(load, 100-percent)   #截取的图片和load原始图对比，0表示完全相似
    self.assertTrue(result)
logger = log.Logger('TestResult//log.log')
def get_element(self,method,TEXT,number):

    '''获取控件元素'''
    if method == "name":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_name(TEXT))
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "class_name":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_class_name(TEXT))
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "css":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_css_selector(TEXT))
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "id":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_id(TEXT))
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "link":
        try:
         # TEXT = is_chinese(TEXT)
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_link_text(TEXT))
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "partial_link":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_partial_link_text(TEXT))
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "tag":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_tag_name(TEXT))
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "xpath":
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_xpath(TEXT))
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "desc":  #content-desc
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_accessibility_id(TEXT))
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "class_names":
        try:
            element = self.driver.find_elements_by_class_name(TEXT)
            element = element[number]
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "elements_css":
        try:
            element = self.driver.find_elements_by_css_selector(TEXT)
            element = element[number]
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "ids":  #('ids','password','881218',0)
        try:
            element = self.driver.find_elements_by_id(TEXT)
            element = element[number]
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "links":
        try:
            element = self.driver.find_elements_by_link_text(TEXT)
            element = element[number]
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "names":
        try:
            element = self.driver.find_elements_by_name(TEXT)
            element = element[number]
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "partial_links":
        try:
            element = self.driver.find_elements_by_partial_link_text(TEXT)
            element = element[number]
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "tags":
        try:
            element = self.driver.find_elements_by_tag_name(TEXT)
            element = element[number]
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "xpaths":
        try:
            element = self.driver.find_elements_by_xpath(TEXT)
            element = element[number]
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)
    elif method == "descs":   #content-desc
        try:
            element = WebDriverWait(self.driver,10).until(lambda x: x.find_elements_by_accessibility_id(TEXT))
            element = element[number]
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            return element
        except Exception,e:
            ErrorLog(self)

def ErrorLog(self):
    Testtime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    '''遇到错误后的处理方式
    '''
    time.sleep(1.5)
    self.driver.get_screenshot_as_file("TestResult\\screenshot\\Failed\\%s.png"%Testtime)
    print logger.war('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
    assertverify()
def assertverify():
    #处理断言是否继续执行和断言失败报告为FAIL
    if command == 'assert':
        self.assertEqual(111,TEXT,u'未找到:\"%s\"'%TEXT)
    elif command == 'verify':
        pass
