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
        print u"========【城际快线流程】============="
        if(len(listdata) <= 0 ):
            assert 0,u"Excel数据库异常"
        for i in range(0,int(len(listdata))):
            #SettingDevice.scroll(self,'up',number=3,times=1000)  #向上滑动屏幕
            print 'Excel中共有：%s 行数据'%(len(listdata))
            APP_InitLogin.init_login(self,i,listdata)      #处理向导和登录
            self.func("id","com.wxws.myticket:id/tv_ticket_cjkx")  #点击城际快线
            #self.func("id","com.wxws.myticket:id/tv_ticket_cjkx","id","com.wxws.myticket:id/etBecity",get_element='scroll')
            self.func("id","com.wxws.myticket:id/etBecity")  #出发地
            self.func('id',"com.wxws.myticket:id/etSearch",send_keys=listdata_chengshi[i]['username'])
            #self.driver.find_element_by_id('com.wxws.myticket:id/etSearch').send_keys(listdata_chengshi[i]['username'])  #获取excel中的存的出发城市
            self.func('class_names','android.widget.TextView',1)   #选择第一个
            #   self.func("id","com.wxws.myticket:id/tv_cancel")
            self.func("id","com.wxws.myticket:id/etEncity")        #到达城市
            self.func('id',"com.wxws.myticket:id/etSearch",send_keys=listdata_chengshi[i]['password'])
            #self.driver.find_element_by_id('com.wxws.myticket:id/etSearch').send_keys(listdata_chengshi[i]['password'])  #获取excel中的存的到达城市
            self.func('class_names','android.widget.TextView',1)  #选择第一个
            self.func("id","layout_departure_time")    #点击时间框
            self.func("xpath",u"//android.widget.TextView[@text='后天']")                   #选择第一个20号(中文一定要加u,要加到最前面才行)
            self.func("id","com.wxws.myticket:id/btnQuery")       #点击查询
            self.func('class_names','android.widget.LinearLayout',1)    #点击线路列表中的第二条线路
            #self.func("ids","com.wxws.myticket:id/layoutStation")       #点击查看地图
            try:
                self.driver.find_element_by_id('com.wxws.myticket:id/layoutStation')#点击查看地图
                self.driver.find_element_by_id('com.wxws.myticket:id/tvTitle')
                #self.func("id","com.wxws.myticket:id/tvTitle")             #点击途径线路，点成功则表示打开了地图，错误则没有打开地图
                self.driver.keyevent("4")
            except Exception,e:
                print "打开地图失败！"
            SettingDevice.scroll(self,'up')  #向上滑动
            #time.sleep(2)
            #self.func('name',"//android.widget.TextView[@text='退票说明']",get_element='is_displayed')
            #self.func('name',"//android.widget.TextView[@text='退票说明']",get_element='is_enabled')
            self.func("id","com.wxws.myticket:id/knows")   #立即预定界面的退票说明
            self.func("id","com.wxws.myticket:id/imgLeft")   #点击返回


            self.func("class_name","android.widget.Button")     #立即预定
            #self.func("id","com.wxws.myticket:id/tv_show_type") #购票类型(默认就是展开的，点击就关闭
            self.func("class_names","android.widget.Button",1)  #点击+号
            self.func("class_names","android.widget.Button")  #点击-号
            self.func("id","com.wxws.myticket:id/layout_Picker") #点击取票人
            self.func('class_names','android.widget.LinearLayout',1) #选第2个联系人
            self.func("id","com.wxws.myticket:id/layoutQuan")   #优惠券
            SettingDevice.scroll(self,'up')  #向上滑动
            try:
                self.func("id","com.wxws.myticket:id/tvRefund_tips")  #退票说明
                tuipiao = self.func("id","com.wxws.myticket:id/refund_tip_1",get_element='text')
                re.search(u"本线路为特价线路(.*)",tuipiao).group()   #能找到不报错说明是特价线路，找不到说明是可退票线路
                self.driver.keyevent('4')   #按返回
                print "当前线路为特价线路"
            except Exception,e:
                print '当前线路为可退票线路'
            #显示金额详情
            self.func("id","com.wxws.myticket:id/rl_desc_price")
            #提交订单
            #self.func("id","com.wxws.myticket:id/btnPay")
            #立即支付
            #self.func("name","    立即支付    ")