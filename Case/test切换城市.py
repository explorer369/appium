# -*- coding:GBK
import logging,os,sys,time,unittest,xlrd,re
import APP_InitLogin,SettingDevice,log,openexcel,AdbTool,InitMySqldb,Initialization
reload(sys)
sys.setdefaultencoding('GBK')
class AndroidTest(unittest.TestCase):
    func = getattr(__import__('find'),'find_name')  
    def setUp(self):
        SettingDevice.Setting_device(self)
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
        print u"========【检查切换城市】============="
        if(len(listdata) <= 0 ):
            assert 0,u"Excel数据库异常"
        for i in range(0,int(len(listdata))):
            print 'Excel中共有：%s 行数据'%(len(listdata))
            APP_InitLogin.huanyingye(self)      #处理向导
            self.func("id","com.wxws.myticket:id/tv_ticket_cjkx")  #点击城际快线
            self.func("id","com.wxws.myticket:id/etBecity")  #出发地
            self.func('id',"com.wxws.myticket:id/etSearch",send_keys=listdata_chengshi[i]['username'])
            self.func('class_names','android.widget.TextView',1)   #选择第一个
            self.func("id","com.wxws.myticket:id/etEncity")        #到达城市
            self.func('id',"com.wxws.myticket:id/etSearch",send_keys=listdata_chengshi[i]['password'])
            self.func('class_names','android.widget.TextView',1)  #选择第一个
            self.func("id","layout_departure_time")    #点击时间框
            self.func("xpath",u"//android.widget.TextView[@text='后天']")                   #选择第一个20号(中文一定要加u,要加到最前面才行)
            print u"===【切换搜索界面的城市】==="
            self.func("id","com.wxws.myticket:id/btnChange")    #点击切换按钮
            StartCityName = self.func('id',"com.wxws.myticket:id/etBecity",get_element="text")   #获取出发城市当前值
            EndCityName = self.func('id',"com.wxws.myticket:id/etEncity",get_element="text")     #获取到达城市当前值
            try:
                if listdata_chengshi[i]['password'] == StartCityName:
                    print u"搜索页点击切换城市正常！\n初始为：%s-%s 切换后为：%s-%s"%(listdata_chengshi[i]['username'],listdata_chengshi[i]['password'],StartCityName,EndCityName)
            except Exception,e:
                print u"搜索页点击切换城市错误\n错误信息为:%s"%e
            self.func("id","com.wxws.myticket:id/btnQuery")       #点击查询