# -*- coding:GBK
import logging,os,sys,time,unittest,xlrd,re
import APP_InitLogin,SettingDevice,log,openexcel,AdbTool,InitMySqldb,Initialization
reload(sys)
sys.setdefaultencoding('GBK')
class AndroidTest(unittest.TestCase):
    func = getattr(__import__('find'),'find_name')  
    def setUp(self):
        SettingDevice.Setting_device(self)
        self.listdata = openexcel.excel_table_byindex('app_data.xls',0)   #��¼�˺ű�
        self.listdata_chengshi = openexcel.excel_table_byindex('data.xls',0) #�������б�
    def tearDown(self):
        try:
            Typewriting = self.func(get_element='available_ime_engines') #��ȡ�ֻ��п��õ����뷨�б�
            self.driver.activate_ime_engine(Typewriting[0])              #�л����뷨Ϊ��һ�����뷨
        except Exception,e:
            print e
        #self.driver.close_app()
        self.driver.quit()       #ִ�����˳����൱��������Ӧ�ã������Ӧ�����ݣ�
    def test12309click(self):
        listdata = self.listdata   
        listdata_chengshi = self.listdata_chengshi
        print u"========���Ǽʿ������̡�============="
        if(len(listdata) <= 0 ):
            assert 0,u"Excel���ݿ��쳣"
        for i in range(0,int(len(listdata))):
            #SettingDevice.scroll(self,'up',number=3,times=1000)  #���ϻ�����Ļ
            print 'Excel�й��У�%s ������'%(len(listdata))
            APP_InitLogin.init_login(self,i,listdata)      #�����򵼺͵�¼
            self.func("id","com.wxws.myticket:id/tv_ticket_cjkx")  #����Ǽʿ���
            #self.func("id","com.wxws.myticket:id/tv_ticket_cjkx","id","com.wxws.myticket:id/etBecity",get_element='scroll')
            self.func("id","com.wxws.myticket:id/etBecity")  #������
            self.func('id',"com.wxws.myticket:id/etSearch",send_keys=listdata_chengshi[i]['username'])
            #self.driver.find_element_by_id('com.wxws.myticket:id/etSearch').send_keys(listdata_chengshi[i]['username'])  #��ȡexcel�еĴ�ĳ�������
            self.func('class_names','android.widget.TextView',1)   #ѡ���һ��
            #   self.func("id","com.wxws.myticket:id/tv_cancel")
            self.func("id","com.wxws.myticket:id/etEncity")        #�������
            self.func('id',"com.wxws.myticket:id/etSearch",send_keys=listdata_chengshi[i]['password'])
            #self.driver.find_element_by_id('com.wxws.myticket:id/etSearch').send_keys(listdata_chengshi[i]['password'])  #��ȡexcel�еĴ�ĵ������
            self.func('class_names','android.widget.TextView',1)  #ѡ���һ��
            self.func("id","layout_departure_time")    #���ʱ���
            self.func("xpath",u"//android.widget.TextView[@text='����']")                   #ѡ���һ��20��(����һ��Ҫ��u,Ҫ�ӵ���ǰ�����)
            self.func("id","com.wxws.myticket:id/btnQuery")       #�����ѯ
            self.func('class_names','android.widget.LinearLayout',1)    #�����·�б��еĵڶ�����·
            #self.func("ids","com.wxws.myticket:id/layoutStation")       #����鿴��ͼ
            try:
                self.driver.find_element_by_id('com.wxws.myticket:id/layoutStation')#����鿴��ͼ
                self.driver.find_element_by_id('com.wxws.myticket:id/tvTitle')
                #self.func("id","com.wxws.myticket:id/tvTitle")             #���;����·����ɹ����ʾ���˵�ͼ��������û�д򿪵�ͼ
                self.driver.keyevent("4")
            except Exception,e:
                print "�򿪵�ͼʧ�ܣ�"
            SettingDevice.scroll(self,'up')  #���ϻ���
            #time.sleep(2)
            #self.func('name',"//android.widget.TextView[@text='��Ʊ˵��']",get_element='is_displayed')
            #self.func('name',"//android.widget.TextView[@text='��Ʊ˵��']",get_element='is_enabled')
            self.func("id","com.wxws.myticket:id/knows")   #����Ԥ���������Ʊ˵��
            self.func("id","com.wxws.myticket:id/imgLeft")   #�������


            self.func("class_name","android.widget.Button")     #����Ԥ��
            #self.func("id","com.wxws.myticket:id/tv_show_type") #��Ʊ����(Ĭ�Ͼ���չ���ģ�����͹ر�
            self.func("class_names","android.widget.Button",1)  #���+��
            self.func("class_names","android.widget.Button")  #���-��
            self.func("id","com.wxws.myticket:id/layout_Picker") #���ȡƱ��
            self.func('class_names','android.widget.LinearLayout',1) #ѡ��2����ϵ��
            self.func("id","com.wxws.myticket:id/layoutQuan")   #�Ż�ȯ
            SettingDevice.scroll(self,'up')  #���ϻ���
            try:
                self.func("id","com.wxws.myticket:id/tvRefund_tips")  #��Ʊ˵��
                tuipiao = self.func("id","com.wxws.myticket:id/refund_tip_1",get_element='text')
                re.search(u"����·Ϊ�ؼ���·(.*)",tuipiao).group()   #���ҵ�������˵�����ؼ���·���Ҳ���˵���ǿ���Ʊ��·
                self.driver.keyevent('4')   #������
                print "��ǰ��·Ϊ�ؼ���·"
            except Exception,e:
                print '��ǰ��·Ϊ����Ʊ��·'
            #��ʾ�������
            self.func("id","com.wxws.myticket:id/rl_desc_price")
            #�ύ����
            #self.func("id","com.wxws.myticket:id/btnPay")
            #����֧��
            #self.func("name","    ����֧��    ")