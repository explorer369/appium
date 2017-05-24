# coding=GBK
import os,sys,time,re,xlrd,SettingDevice
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
def huanyingye(self):
    try:  #关闭活动弹窗
        while self.func('xpath',"//android.widget.ImageView[@index='0']",get_element='is_displayed') == True:  #先判断元素是否可见，处理出现加载中
            #self.func('1000','1000','20','1000',times=500,get_element='swipe',nb=3)   #向左滑动3次
            SettingDevice.scroll(self,'left',number=3,times=500)
            self.func('id',"com.wxws.myticket:id/imgOpen")                            #立即体验
            break                                                                    #执行后跳出循环
        else:
            time.sleep(0.5)
    except Exception,e:
        pass
    try:  #关闭下载APP弹窗
        time.sleep(3)
        if self.func('ids',"com.wxws.myticket:id/tabView",get_element='is_displayed') == False:   #找不到购票按钮说明有弹窗
            self.driver.keyevent('4')   #按返回键取消弹框
    except Exception,e:
        pass
def init_login(self,i,listdata):
    for g in range(1,2):
        huanyingye(self)   #处理欢迎页和弹窗
        self.func('id',"com.wxws.myticket:id/tvMytext")          #个人
        self.func('id',"com.wxws.myticket:id/layout_top_login")  #登录按钮
        def intstrusername():
            #处理excel文档读取转换为int
            try:
                username = listdata[i]['username']
                username = int(username)
                return username
            except:
                username = listdata[i]['username']
                return username
        def intstrpassword():
            #处理excel文档读取转换为int
            try:
                password = listdata[i]['password']
                password = int(password)
                return password
            except:
                password = listdata[i]['password']
                return password
        username = intstrusername()
        password = intstrpassword()
        print username,password
        self.func('id',"com.wxws.myticket:id/user_name",send_keys=username)
        self.func('id',"com.wxws.myticket:id/pwd",send_keys=password)
        self.func('id',"com.wxws.myticket:id/login")
        try:
            #self.func('name',u"欢迎来到12308汽车票")# 这样就点击进去了
            #WebDriverWait(self.driver,3).until(lambda x: x.find_element_by_xpath("//*[contains(.,'欢迎来到')]"))
            self.func('ids','com.wxws.myticket:id/tabView')   #点击购票
            break
        except:
            self.driver.keyevent('4')  #返回到登录页
            continue
