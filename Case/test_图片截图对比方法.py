# -*- coding:GBK
import logging,os,sys,time,unittest,xlrd,re
import APP_InitLogin,SettingDevice,log,openexcel,AdbTool,InitMySqldb,Initialization,extend
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
reload(sys)
sys.setdefaultencoding('GBK')
class AndroidTest(unittest.TestCase):
    func = getattr(__import__('find'),'find_name')  
    def setUp(self):
        SettingDevice.Setting_device(self)
        self.extend = extend.Appium_Extend(self.driver)      #调用extend文件下的Appium_Extend类
        self.listdata = openexcel.excel_table_byindex('app_data.xls',0)   #登录账号表
        self.listdata_chengshi = openexcel.excel_table_byindex('data.xls',0) #搜索城市表
    def tearDown(self):
        try:
            Typewriting = self.func(get_element='available_ime_engines') #获取手机中可用的输入法列表
            self.driver.activate_ime_engine(Typewriting[0])              #切换输入法为第一个输入法
        except Exception,e:
            print e
        #self.driver.close_app()
        self.driver.quit()       #执行完退出后相当于重置了应用（清除了应用数据）
    def test12309click(self):
        listdata = self.listdata   
        listdata_chengshi = self.listdata_chengshi
        print u"========【订单详情页优惠券】============="
        if(len(listdata) <= 0 ):
            assert 0,u"Excel数据库异常"
        for i in range(0,int(len(listdata))):
            print 'Excel中共有：%s 行数据'%(len(listdata))
            #APP_InitLogin.init_login(self,i,listdata)      #处理向导和登录
            SettingDevice.scroll(self,'left',number=3,times=1000)  #向上滑动屏幕
            SettingDevice.get_element_screen(self,"id","com.wxws.myticket:id/etBecity",name="fff")  #截图控件图片
            #SettingDevice.test_same_as(self,"id","com.wxws.myticket:id/etBecity")  #截控件图为上面保存的对比
            self.func("id","com.wxws.myticket:id/etBecity")  #出发地
            self.func('id',"com.wxws.myticket:id/etSearch",send_keys=listdata_chengshi[i]['username'])
            self.func('class_names','android.widget.TextView',1)   #选择第一个
            self.func("id","com.wxws.myticket:id/etEncity")        #到达城市
            self.func('class_names','android.widget.TextView',1)   #选择第一个

            self.func('id',"com.wxws.myticket:id/etSearch",send_keys=listdata_chengshi[i]['password'])
            self.func('class_names','android.widget.TextView',1)  #选择第一个
            SettingDevice.test_same_as(self,"id","com.wxws.myticket:id/etEncity",percent=1)
            '''
            #self.func("id","layout_departure_time")    #点击时间框
            #self.func("xpath",u"//android.widget.TextView[@text='后天']")                   #选择第一个20号(中文一定要加u,要加到最前面才行)
            self.func("id","com.wxws.myticket:id/btnQuery")       #点击查询
            self.func('class_names','android.widget.LinearLayout',number=2)    #点击线路列表中的第二条线路
            self.func("xpath",u"//android.widget.TextView[@text='票源充足']")  #点击票源充足的班次
            self.func("id","com.wxws.myticket:id/layoutQuan")   #优惠券
            if SettingDevice.find_toast(self,By.XPATH,u".//*[contains(@text,'没有可使用的优惠券')]") :
                print u"当前账号没有可用的优惠券"
            else:
                print u"有可用的优惠券"
            '''