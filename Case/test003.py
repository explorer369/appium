# -*- coding:GBK
import logging,os,sys,time,unittest,xlrd,threading
import APP_InitLogin,SettingDevice,log,openexcel,AdbTool,InitMySqldb,Initialization
from appium import webdriver
reload(sys)
sys.setdefaultencoding('GBK')
tt = []
def server():
    deviceids = Initialization.duo_finddevices()
    print deviceids
    for i in range(len(deviceids)):
        desired_caps = SettingDevice.duo_Setting_device()
        wzj = webdriver.Remote('http://localhost:'+str(4723+i)+'/wd/hub', desired_caps)
        dingwei = AndroidTest(wzj)
        t = threading.Thread(target=dingwei)
        tt.append(t)
class AndroidTest(unittest.TestCase):
    func = getattr(__import__('find'),'find_name')  #func()# 相当于执行find.py的foo函数
    def __init__(self,wzj):
        print wzj
        self.driver = wzj
    def setUp(self):
        #SettingDevice.Setting_device(self)   #获取连上的手机并初始化
        self.listdata = openexcel.excel_table_byindex('app_data.xls',0)
        self.listdata_chengshi = openexcel.excel_table_byindex('data.xls',0)
        adb = AdbTool.AdbTools()  #实例化，调用adb类
        #SettingDevice.Setting_device(self)   #获取连上的手机并初始化
    def tearDown(self):
        try:
            Typewriting = self.func(get_element='available_ime_engines') #获取手机中可用的输入法列表
            self.driver.activate_ime_engine(Typewriting[0])              #切换输入法为第一个输入法
        except Exception,e:
            print e
        self.driver.close_app()
        self.driver.quit()       #执行完退出后相当于重置了应用（清除了应用数据）
    def test12309click(self):
        listdata = self.listdata   #调用setup里的局部变量
        listdata_chengshi = self.listdata_chengshi
        print "========【case_0001】============="
        if(len(listdata) <= 0 ):
            assert 0,u"Excel数据库异常"
        for i in range(0,int(len(listdata))):
            #self.driver.keyevent('26')
            #SettingDevice.scroll(self,'left',number=3,times=1000)  #向左滑动屏幕
            #SettingDevice.shoushimima_my(self)
            APP_InitLogin.init_login(self,i,listdata)
            print 'Excel中共有：%s 行数据'%(len(listdata))
            time.sleep(2)
            #self.func('1000','1000','20','1000',times=500,get_element='swipe',nb=3)
            #self.func(get_element='toggle_location_services')
            #time.sleep(5)
            self.func("id","com.wxws.myticket:id/tv_ticket_cjkx")  #点击城际快线
            #self.func("id","com.wxws.myticket:id/tv_ticket_cjkx","id","com.wxws.myticket:id/etBecity",get_element='scroll')
            time.sleep(2)

            self.func("id","com.wxws.myticket:id/etBecity")
            self.driver.find_element_by_id('com.wxws.myticket:id/etSearch').send_keys(listdata_chengshi[i]['username'])
            self.func('class_names','android.widget.TextView',1)
            time.sleep(1)
            #   self.func("id","com.wxws.myticket:id/tv_cancel")
            self.func("id","com.wxws.myticket:id/etEncity")
            self.driver.find_element_by_id('com.wxws.myticket:id/etSearch').send_keys(listdata_chengshi[i]['password'])
            time.sleep(2)
            self.func('class_names','android.widget.TextView',1)
            self.func("id","com.wxws.myticket:id/btnQuery")
            self.func('class_names','android.widget.LinearLayout',1)
            time.sleep(1)
            #     self.func("xpath","//android.widget.TextView[@text='退票说明']")
            #    time.sleep(1)
            #      self.func("id","com.wxws.myticket:id/imgLeft")
            time.sleep(1)
            self.func("class_name","android.widget.Button")
            time.sleep(1)
            self.func("id","com.wxws.myticket:id/layout_Picker")
            time.sleep(1)
            self.func('class_names','android.widget.LinearLayout',1)
server()
for i in tt:
    i.start()