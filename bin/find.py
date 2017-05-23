#coding:GBK
import logging,os,sys,time,traceback
from ConfigParser import ConfigParser
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import log    #导入本地模块
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
def find_name(self,method=None,TEXT=None,number=0,send_keys=None,get_element=None,select_keys=None,nb=None,times=None):   #此处顺序不要改变，参数可以在后面加但不要改
    Testtime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    '''用法：self.find_name('id','com.wxws.myticket:id/rl_notification')
           self.find_name('name','点击')
           self.find_name('class_name','android.widget.TextView')
           self.find_name('class_names','android.widget.TextView',1)
           self.find_name('xpath',"//android.view.View[@index='2']")
    '''
    def duoyuanshu_1():    #获取第一个元素
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
    def duoyuanshu_2():    #获取第二个元素
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
        #处理断言是否继续执行和断言失败报告为FAIL
        if command == 'assert':
            self.assertEqual(111,TEXT,u'未找到:\"%s\"'%TEXT)
        elif command == 'verify':
            pass
        #此处logger和eclipse上输出日志有关联，加到这里会重复

    def click_input(self):
        '''单控件时点击和输入代码
        '''
        logger.info('+PASS+  找到"%s"元素'%TEXT)
        emmm.click()
        time.sleep(1.5)
        self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
        #TEXTbbb = FontColor.printRed(u'%s'.encode("gb2312")%TEXT)
        if number == 0:
            logger.info('+PASS+  点击"%s"元素成功，已保存截图'%TEXT)
        else:
            logger.info('+PASS+  点击第%s个"%s"元素成功，已保存截图'%(number,TEXT))
        #time.sleep(1.5)
    def send_keysaaa(self):
        '''输入框内输入内容zd
        '''
        logger.info('+PASS+  找到"%s"元素'%TEXT)
        emmm.send_keys(send_keys)
        time.sleep(1.5)
        self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
        logger.info('+PASS+  输入"%s"成功，已保存截图'%send_keys)
        return send_keys
        #time.sleep(1.5)
    def ErrorLog(self):
        '''遇到错误后的处理方式
        '''
        time.sleep(1.5)
        self.driver.get_screenshot_as_file("TestResult\\screenshot\\Failed\\%s.png"%Testtime)
        print logger.war('+FAIL+  未找到"%s"元素， 已截图'%TEXT)
        assertverify()
        #time.sleep(1.5)
    def gettext(self):
        #获取元素的文本值('id',"startLogin"，get_element='text')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            abc = emmm.text
            #abc = FontColor.printRed(u"%s".encode("gb2312")%abc)
            logger.info('+PASS+  获取==="%s"===元素信息成功，已返回结果'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  获取元素text信息失败，请检查该控件是否支持')
             raise Exception()   #手动触发异常，让此处理抛出异常

    def clear_element(self):  #####
        #清除输入框的文本值('id',"startLogin"，get_element='clear')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            emmm.clear()
            logger.info('+PASS+  清除输入框"%s"元素内容成功'%TEXT)
            self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
        except Exception, e:
             logger.war('+FAIL+  清除输入框"%s"元素内容失败，请确认传入的控件是输入框？'%TEXT)
             raise Exception()   #手动触发异常，让此处理抛出异常
    def get_location(self):
        #获取元素坐标('id',"startLogin"，get_element='location')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            abc = emmm.location
            x = emmm.location.get('x')
            y = emmm.location.get('y')
            logger.info('+PASS+  获取==="%s"===元素坐标值成功，已返回结果'%abc)
            logger.info('+PASS+  该无素的X坐标为"%s" Y坐标为"%s"，已返回结果(元素坐标,X,Y)'%(x,y))
            return abc,x,y
        except Exception, e:
             logger.war('+FAIL+  获取"%s"元素坐标值失败，请检查传入的控件是否正确'%TEXT)
             raise Exception()   #手动触发异常，让此处理抛出异常
    def get_rect(self):
        #获取元素的大小和位置的字典('id',"startLogin"，get_element='rect')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            abc = emmm.rect
            logger.info('+PASS+  值为==="%s"===元素的大小和位置的字典成功，已返回结果'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  获取"%s"元素的大小和位置的字典失败'%TEXT)
             raise Exception()   #手动触发异常，让此处理抛出异常
    def get_submit(self):
        #提交表单('id',"startLogin"，get_element='submit')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            emmm.submit()
            self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  提交表单内容成功，已截图，提交的元素为"%s"'%TEXT)
        except Exception, e:
            logger.war('+FAIL+  提交表单内容失败，请检查该元素是否支持表单提交，已截图，要提交的元素为"%s"'%TEXT)
            raise Exception()   #手动触发异常，让此处理抛出异常

    def my_get_attribute(self):
        #获取元素的属性值('id',"startLogin"，get_element='get_attribute')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            abc = emmm.get_attribute(TEXT)
            logger.info('+PASS+  获取元素属性值成功,属性值为==="%s"===，已返回结果！'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  获取"%s"元素属性值失败，请检查传入的元素正确！'%TEXT)
             raise Exception()   #手动触发异常，让此处理抛出异常


    def my_context_click(self):
        #右击元素('id',"startLogin"，get_element='context_click')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            ActionChains(self.driver).context_click(emmm).perform()
            self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  右击该元素成功！')
        except Exception, e:
            logger.war('+FAIL+  右击该元素失败，请确认该元素可被右击！')
            raise Exception()   #手动触发异常，让此处理抛出异常
    def my_double_click(self):
        #双击元素('id',"startLogin"，get_element='double_click')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            ActionChains(self.driver).double_click(emmm).perform()
            self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
            logger.info('+PASS+  双击该元素成功！')
        except Exception, e:
            logger.war('+FAIL+  双击该元素失败，请确认该元素可被双击！')
            raise Exception()   #手动触发异常，让此处理抛出异常
    def my_move_to_element(self):
        #鼠标悬停在一个元素上('id',"startLogin"，get_element='move_to_element')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            ActionChains(self.driver).move_to_element(emmm).perform()
            logger.info('+PASS+  鼠标悬停在该元素上成功！')
        except Exception, e:
             logger.war('+FAIL+  鼠标悬停在该元素上失败，请确认该元素是否支持！')
             raise Exception()   #手动触发异常，让此处理抛出异常
    def select_down(self):
        #选择下拉框里的内容('id',"startLogin"，get_element='select',number=1)
        #('id',"startLogin"，get_element='select',select_keys=u'深圳')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            if select_keys == None:
                Select(emmm).select_by_index(number)
                self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
                logger.info('+PASS+  选择第"%s"个元素成功！(从0开始计算)'%number)
            else:
                Select(emmm).select_by_visible_text(select_keys)
                self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
                logger.info('+PASS+  选择"%s"成功！'%select_keys)
        except Exception, e:
             logger.war('+FAIL+  执行选择元素失败，请确认该元素支持下拉选择！')
             raise Exception()   #手动触发异常，让此处理抛出异常
    # 回到顶部
    def scroll_top(self):
        #self.func(get_element='scroll_top')
        try:
            if self.driver.name == "chrome":
                js = "var q=document.body.scrollTop=0"
            else:
                js = "var q=document.documentElement.scrollTop=0"
            return self.driver.execute_script(js)
        except Exception, e:
             logger.war('+FAIL+  执行回到顶部失败！')
             #raise Exception()   #手动触发异常，让此处理抛出异常，注释后执行失败也继续执行后面的
    # 拉到底部
    def scroll_foot(self):
        #self.func(get_element='scroll_foot')
        try:
            if self.driver.name == "chrome":
                js = "var q=document.body.scrollTop=10000"
            else:
                js = "var q=document.documentElement.scrollTop=10000"
            return self.driver.execute_script(js)
        except Exception,e:
            logger.war('+FAIL+  执行拉到底部失败！')
            #raise Exception()   #手动触发异常，让此处理抛出异常，注释后执行失败也继续执行后面的
    def scroll_element(self):
        #移动到元素element对象的“顶端”与当前窗口的“顶部”对齐
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", emmm)
            logger.info('+PASS+ 元素对象的“顶端”与当前窗口的“顶部”对齐成功！"%s"'%TEXT)
        except Exception,e:
            logger.war('+FAIL+ 元素对象的“顶端”与当前窗口的“顶部”对齐失败！"%s"'%TEXT)
    def scroll_element_foot(self):
        #移动到元素element对象的“底端”与当前窗口的“底部”对齐
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            self.driver.execute_script("arguments[0].scrollIntoView(false);", emmm)
            logger.info('+PASS+ 元素对象的“底端”与当前窗口的“底部”对齐成功！"%s"'%TEXT)
        except Exception,e:
            logger.war('+FAIL+ 元素对象的“底端”与当前窗口的“底部”对齐失败！"%s"'%TEXT)
    def click_scroll_element(self):
        #点击元素下滑一点('id',"startLogin",number=0,get_element='click_scroll_element')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            for i in range(0,number):
                emmm.send_keys(Keys.DOWN)
                time.sleep(0.3)#加不加都没有问题，因为上面的是智能等待
                logger.info('+PASS+ 点击元素下滑成功！次数：%s次'%number)
        except Exception,e:
            logger.war('+FAIL+ 击元素"%s"下滑失败！'%TEXT)
            traceback.print_exc()

    #下面两个为多元素时处理方支式
    def select_down_s(self):
        #选择多元素下拉框里的内容('ids',"startLogin"，get_element='select',number=1,nb=1)
        #('ids',"startLogin"，get_element='select',number=0,select_keys=u'深圳')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            if select_keys == None:
                Select(emmm).select_by_index(nb)
                self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
                logger.info('+PASS+  选择第"%s"个元素成功！(从0开始计算)'%nb)
            else:
                Select(emmm).select_by_visible_text(select_keys)
                self.driver.get_screenshot_as_file("TestResult\\screenshot\\Passed\\%s.png"%Testtime)
                logger.info('+PASS+  选择"%s"成功！'%select_keys)
        except Exception, e:
             logger.war('+FAIL+  执行选择元素失败，请确认该元素支持下拉选择！')
             raise Exception()   #手动触发异常，让此处理抛出异常
    def click_scroll_elements(self):
        #点击元素下滑一点('ids',"startLogin"，get_element='click_scroll_element',number=1,nb=1)
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            for i in range(0,nb):
                emmm.send_keys(Keys.DOWN)
                time.sleep(0.3)#加不加都没有问题，因为上面的是智能等待
                logger.info('+PASS+ 点击元素下滑成功！次数：%s次'%nb)
        except Exception,e:
            logger.war('+FAIL+ 击元素"%s"下滑失败！'%TEXT)
            traceback.print_exc()
    def removeAttr_readonly_sendkeys(self):
        #去除只读属性并赋值('css',"input[name='outBusStartTime']"，get_element='readonly',send_keys='2016-12-14')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            js="$(\"%s\").removeAttr('readonly');$(\"%s\").attr('value','%s')%(TEXT,TEXT,send_keys)"
            self.driver.execute_script(js)
            logger.info('+PASS+ 去除元素属性成功！')
        except Exception,e:
            logger.war('+FAIL+ 去除元素属性失败！')
            traceback.print_exc()
    def removeAttr_readonly(self):
        #去除只读属性('css',"input[name='outBusStartTime']"，get_element='readonly')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            self.driver.execute_script("$(\"%s\").removeAttr('readonly')"%TEXT)
            logger.info('+PASS+ 去除元素属性成功！')
        except Exception,e:
            logger.war('+FAIL+ 去除元素属性失败！')
            traceback.print_exc()

    def removeAttr_send_keys(self):
        #去除只读属性并赋值('css',"input[name='outBusStartTime']"，get_element='readonly',send_keys='2016-12-12')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            self.driver.execute_script("$(\"%s\").removeAttr('readonly');$(\"%s\").attr('value',\"%s\")"%(TEXT,TEXT,send_keys))
            logger.info('+PASS+ 去除元素属性成功！')
        except Exception,e:
            logger.war('+FAIL+ 去除"%s"元素属性失败')
            traceback.print_exc()


    def my_pinch(self):
        #在元素上执行模拟双指捏（缩小操作）（'id',"dfas",get_element="pinch"）
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            self.driver.pinch(emmm)
            logger.info('+PASS+ 在元素上执行模拟双指捏成功！')
        except Exception,e:
            logger.war('+FAIL+ 在元素上执行模拟双指捏失败！')
            traceback.print_exc()
    def my_zoom(self):
        #在元素上执行放大操作（'id',"dfas",get_element="zoom"）
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            self.driver.zoom(emmm)
            logger.info('+PASS+ 在元素上执行放大操作成功！')
        except Exception,e:
            logger.war('+FAIL+ 在元素上执行放大操作失败！')
            traceback.print_exc()
    def my_tagName(self):
        #返回元素的tagName('id',"startLogin"，get_element='tagname')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            abc = emmm.tag_name()
            logger.info('+PASS+  该元素的tagname是==="%s"===，且已返回结果！'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  传入的"%s"元素对象没有属性的标签名，请传入正确的元素！'%TEXT)
             raise Exception()   #手动触发异常，让此处理抛出异常
    def my_is_selected(self):
        #判断元素是否被选中('id',"startLogin"，get_element='is_selected')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            abc = emmm.is_selected()
            if abc == True:
                logger.info('+PASS+  "%s"是==="%s"===选中状态，且已返回结果！（True）'%TEXT)
            else:
                logger.info('+PASS+  "%s"是==="%s"===未选中状态，且已返回结果！（False）'%TEXT)
            return abc
        except Exception, e:
             logger.war('+FAIL+  传入"%s"元素执行失败，请检查传入的元素正确！'%TEXT)
             raise Exception()   #手动触发异常，让此处理抛出异常
    def my_is_enabled(self):
        #判断元素是否被使用('id',"startLogin"，get_element='is_enabled')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            abc = emmm.is_enabled()
            if abc == True:
                logger.info('+PASS+  该元素是==="%s"===可使用状态，且已返回结果！（True）'%TEXT)
            else:
                logger.info('+PASS+  该元素==="%s"===不是被使用状态，且已返回结果！（False）'%TEXT)
            return abc
        except Exception, e:
             logger.war('+FAIL+  传入"%s"元素执行失败，请检查传入的元素正确！'%TEXT)
             raise Exception()   #手动触发异常，让此处理抛出异常
    def my_is_displayed(self):
        #判断元素是否显示('id',"startLogin"，get_element='is_displayed')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            abc = emmm.is_displayed()
            if abc == True:
                logger.info('+PASS+  该元素==="%s"===是可见状态，且已返回结果！（True）'%TEXT)
            else:
                logger.info('+PASS+  该元素==="%s"===是不可见状态，且已返回结果！（False）'%TEXT)
            return abc
        except Exception, e:
             logger.war('+FAIL+  传入"%s"元素执行失败，请检查传入的元素正确！'%TEXT)
             raise Exception()   #手动触发异常，让此处理抛出异常
    def my_size(self):
        #返回元素的大小('id',"startLogin"，get_element='size')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            abc = emmm.size
            logger.info('+PASS+  该元素的大小为==="%s"===，且已返回结果！'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  传入"%s"元素执行失败，请检查传入的元素正确！'%TEXT)
             raise Exception()   #手动触发异常，让此处理抛出异常
    def css_name(self):
        #获取CSS的属性值('id',"startLogin"，get_element='css')
        try:
            logger.info('+PASS+  找到"%s"元素'%TEXT)
            abc = emmm.value_of_css_property(TEXT)
            logger.info('+PASS+  获取CSS元素属性值成功，该属性为==="%s"===已返回结果'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  获取"%s"元素属性值失败，你传入的是css_name？'%TEXT)
             raise Exception()   #手动触发异常，让此处理抛出异常
    def panduanfangfa(self):   #带元素时
            if send_keys == None and get_element == None:
                click_input(self)
            elif send_keys != None and get_element == None:
                return send_keysaaa(self)
            elif get_element == 'text':
                return gettext(self)                     #获取元素的文本值
            elif get_element == 'clear':
                clear_element(self)
            elif get_element == 'location':
                return get_location(self)                #获取元素坐标
            elif get_element == 'submit':
                get_submit(self)
            elif get_element == 'css':
                return css_name(self)                    #获取CSS的属性值
            elif get_element == 'get_attribute':
                return my_get_attribute(self)            #获取元素的属性值
            elif get_element == 'is_selected':
                return my_is_selected(self)              #判断元素是否被选中
            elif get_element == 'size':
                return my_size(self)                     #返回元素的大小
            elif get_element == 'is_displayed':
                return my_is_displayed(self)             #判断元素是否显示
            elif get_element == 'is_enabled':
                return my_is_enabled(self)               #判断元素是否被使用
            elif get_element == 'tagname':
                return my_tagName(self)                  #返回元素的tagname
            elif get_element == 'context_click':
                my_context_click(self)                   #右击元素
            elif get_element == 'double_click':
                my_double_click(self)                    #双击元素
            elif get_element == 'move_to_element':
                my_move_to_element(self)                 #鼠标悬停在一个元素上
            elif get_element == 'select':
                select_down(self)                       #选择下拉框里的内容
            elif get_element == "scroll_top":
                scroll_top(self)                        #滚动到顶部
            elif get_element == "scroll_foot":
                scroll_foot(self)                       #滚动到底部
            elif get_element == "scroll_element":
                scroll_element(self)                    #移动到元素element对象的“顶端”与当前窗口的“顶部”对齐
            elif get_element == "scroll_element_foot":
                scroll_element_foot(self)               #移动到元素element对象的“底端”与当前窗口的“底部”对齐
            elif get_element == "click_scroll_element" and number !=0 :   #点击元素下滑一点
                click_scroll_element(self)
            elif get_element == 'select' and nb != None:
                select_down_s(self)  #选多控件number，选第几个nb                 #选择多元素下拉框里的内容
            elif get_element == 'click_scroll_element' and nb != None:
                click_scroll_elements(self)   #选多控件number，选第几个nb       #点击元素下滑一点
            elif get_element == 'readonly' and send_keys == None:
                removeAttr_readonly(self)                          #去除只读属性
            elif get_element == 'readonly' and send_keys != None:  #去除了属性并赋值
                removeAttr_send_keys(self)
            elif get_element == "pinch":
                my_pinch(self)
            elif get_element == "zoom":
                my_zoom(self)
            elif get_element == "rect":   #获取元素大小和位置的字典
                get_rect(self)
    def my_contexts(self):
        #返回当前会话中的上下文，使用后可以识H5页面的控件(get_element='contexts')
        try:
            abc = self.driver.contexts
            logger.info('+PASS+  获取==="%s"===当前会话中的上下文成功，已返回结果'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  获取当前会话中的上下文失败')
             raise Exception()
    def my_current_context(self):
        #返回当前会话中的上下文，使用后可以识H5页面的控件(get_element='current_context')
        try:
            abc = self.driver.current_context
            logger.info('+PASS+  获取==="%s"===当前会话中的上下文成功，已返回结果'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  获取当前会话中的上下文失败')
             raise Exception()
    def my_reset(self):
        #重置应用（类似删除应用数据）(get_element='reset')
        try:
            self.driver.reset()
            logger.info('+PASS+  执行重置应用操作成功！')
        except Exception, e:
             logger.war('+FAIL+  执行重置应用操作失败！')
             raise Exception()
    def my_hide_keyboard(self):
        #隐藏键盘（IOS使用key_name隐藏，安卓不使用参数）(get_element='hide_keyboard')
        try:
            self.driver.hide_keyboard()
            logger.info('+PASS+  执行隐藏键盘成功！')
        except Exception, e:
             logger.war('+FAIL+  执行隐藏键盘失败！')
             raise Exception()
    def my_current_activity(self):
        #返回当前会话中的上下文，使用后可以识H5页面的控件(get_element='current_activity')
        try:
            abc = self.driver.current_activity()
            logger.info('+PASS+  获取==="%s"===当前activity成功，已返回结果'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  获取当前的activity失败！')
             raise Exception()
    def my_shake(self):
        #摇一摇手机(get_element='shake')
        try:
            self.driver.shake()
            logger.info('+PASS+  摇一摇手机成功！')
        except Exception, e:
             logger.war('+FAIL+  摇一摇手机失败！')
             raise Exception()
    def my_open_notifications(self):
        #打开系统通知栏(get_element='open_notifications')
        try:
            self.driver.open_notifications()
            logger.info('+PASS+  打开系统通知栏成功！')
        except Exception, e:
             logger.war('+FAIL+  打开系统通知栏失败！')
             raise Exception()
    def my_network_connection(self):
        #返回网络类型数值(get_element='network_connection')
        try:
            abc = self.driver.network_connection
            logger.info('+PASS+  获取==="%s"===网络类型数值成功，已返回结果'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  返回网络类型数值失败！')
             raise Exception()
    def my_available_ime_engines(self):
        #返回安卓设备可用的输入法(get_element='available_ime_engines')
        try:
            abc = self.driver.available_ime_engines
            logger.info('+PASS+  获取==="%s"===安卓可用的输入法成功，已返回结果'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  获取安卓可用的输入法失败！')
             raise Exception()
    def my_is_ime_active(self):
        #检查安卓设备是否输入法服务活动(get_element='is_ime_active')
        try:
            abc = self.driver.is_ime_active()
            logger.info('+PASS+  获取==="%s"===安卓设备是否有输入法服务活动成功，已返回结果'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  获取安卓设备是否有输入法服务活动失败！')
             raise Exception()
    def my_deactivate_ime_engine(self):
        #关闭安卓当前的输入法(get_element='deactivate_ime_engine')
        try:
            self.driver.deactivate_ime_engine()
            logger.info('+PASS+  关闭安卓当前的输入法成功！')
        except Exception, e:
             logger.war('+FAIL+  关闭安卓当前的输入法失败！')
             raise Exception()
    def my_active_ime_engine(self):
        #返回当前输入法的包名(get_element='active_ime_engine')
        try:
            abc = self.driver.active_ime_engine
            logger.info('+PASS+  获取==="%s"===返回当前输入法的包名成功，已返回结果'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  返回当前输入法的包名失败！')
             raise Exception()
    def my_current_url(self):
        #获取当前页面的网址(get_element='current_url')
        try:
            abc = self.driver.current_url
            logger.info('+PASS+  当前页面的网址为:%s'%abc)
        except Exception, e:
             logger.war('+FAIL+  获取当前页面的网址失败！')
             raise Exception()
    def my_page_source(self):
        #返回当前页面的源(get_element='page_source')
        try:
            abc = self.driver.page_source
            logger.info('+PASS+  获取==="%s"===返回当前页面的源成功，已返回结果'%abc)
            return abc
        except Exception, e:
             logger.war('+FAIL+  返回当前页面的源失败！')
             raise Exception()
    def my_scroll(self,emmm1,emmm2):
        #将元素1滚动到目标元素2("id","com.wxws.myticket:id/tv_ticket_cjkx","id","com.wxws.myticket:id/etBecity",get_element='scroll')
        try:
            self.driver.scroll(emmm1,emmm2)
            logger.info('+PASS+  从元素1滚动到元素2成功！')
        except Exception, e:
             print e
             logger.war('+FAIL+  从元素1滚动到元素2失败！')
             raise Exception()
    def my_drag_and_drop(self,emmm1,emmm2):
        #从元素1拖动到元素2(get_element='drag_and_drop')
        try:
            self.driver.drag_and_drop(emmm1,emmm2)
            logger.info('+PASS+  从元素1拖动到元素2成功！')
        except Exception, e:
             logger.war('+FAIL+  从元素1拖动到元素2失败！')
             raise Exception()
    def my_swipe(self):
        #从A点滑动至B点，滑动时间为毫秒('1000','1000','20','1000',times=500,get_element='swipe',nb=4)
        try:
            if nb == None:   #如果未传入nb次数时，设一个默认值
                self.driver.swipe(method,TEXT,number,send_keys,times)
                logger.info('+PASS+  从坐标1滑动到坐标2成功！')
            else:
                for i in range(0,nb):
                    self.driver.swipe(method,TEXT,number,send_keys,times)
                    logger.info('+PASS+  从坐标1滑动到坐标2成功！')
                    time.sleep(1)    #每滑动一条暂停1S，避免性能差的手机在同一页滑动
        except Exception, e:
             logger.war('+FAIL+  从坐标1滑动到坐标2失败！')
             raise Exception()
    def my_flick(self):
        #按住A坐标点后快速滑动至B坐标点('1000','1000','20','1000',get_element='flick')
        try:
            self.driver.flick(method,TEXT,number,send_keys)
            logger.info('+PASS+  从坐标A点快速滑动到坐标B点成功！')
        except Exception, e:
             logger.war('+FAIL+  从坐标A点快速滑动到坐标B点失败！')
             raise Exception()
    def my_set_location(self):
        #设置设备的经纬度('1000','1000','20',get_element='set_location')
        try:
            self.driver.set_location(method,TEXT,number)
            logger.info('+PASS+  设置设备的经纬度成功(%s,%s,%s)！'%(method,TEXT,number))
        except Exception, e:
             logger.war('+FAIL+  设置设备的经纬度失败！')
             raise Exception()
    def my_toggle_location_services(self):
        #打开安卓设备上的位置定位设置(get_element='toggle_location_services')
        try:
            self.driver.toggle_location_services()
            logger.info('+PASS+  打开安卓设备上的位置定位设置成功！')
        except Exception, e:
             print e
             logger.war('+FAIL+  打开安卓设备上的位置定位设置失败！')
             #raise Exception()     #让失败了也继续执行
    def NOpanduanfangfa(self):   #不带元素时
            if get_element == "contexts":
                return my_contexts(self)            #返回的是列表
            elif get_element == "current_context":
                return my_current_context(self)    #返回的是字符串
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
            elif get_element == "active_ime_engine":   #返回当前输入法的包名
                return my_active_ime_engine(self)
            elif get_element == "current_url":     #获取当前页面的网址
                return my_current_url(self)
            elif get_element == "page_source":    #获取当前页面的源
                return my_page_source(self)
    #处理多个元素时的方法
    if get_element == 'scroll':
        emmm1 = duoyuanshu_1()
        emmm2 = duoyuanshu_2()
        my_scroll(self,emmm1,emmm2)          #从元素1滚动到元素2
    elif get_element == 'drag_and_drop':
        emmm1 = duoyuanshu_1()
        emmm2 = duoyuanshu_2()
        my_drag_and_drop(self,emmm1,emmm2)  #将元素origin_el拖到目标元素destination_el
    elif get_element == "swipe":
        my_swipe(self)                      #多A点滑动到B点
    elif get_element == "flick":
        my_flick(self)                      #按住A点后快速滑动至B点
    elif get_element == "set_location":
        my_set_location(self)               #设置设备的经纬度
    elif get_element == "toggle_location_services":
        my_toggle_location_services(self)      #打开安卓设备上的位置定位设置




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
    elif get_element != None:    #get_element带值时执行不带元素的方法
        try:
            return NOpanduanfangfa(self)
        except Exception,e:
            ErrorLog(self)
    else:
        raise Exception('你输入的控件属性名错误，请检查！')
