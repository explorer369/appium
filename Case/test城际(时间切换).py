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
        print u"========������л����С�============="
        if(len(listdata) <= 0 ):
            assert 0,u"Excel���ݿ��쳣"
        for i in range(0,int(len(listdata))):
            print 'Excel�й��У�%s ������'%(len(listdata))
            APP_InitLogin.huanyingye(self)      #����ӡҳ
            self.func("id","com.wxws.myticket:id/tv_ticket_cjkx")  #����Ǽʿ���
            self.func("id","com.wxws.myticket:id/etBecity")  #������
            self.func('id',"com.wxws.myticket:id/etSearch",send_keys=listdata_chengshi[i]['username'])
            self.func('class_names','android.widget.TextView',1)   #ѡ���һ��
            self.func("id","com.wxws.myticket:id/etEncity")        #�������
            self.func('id',"com.wxws.myticket:id/etSearch",send_keys=listdata_chengshi[i]['password'])
            self.func('class_names','android.widget.TextView',1)  #ѡ���һ��
            #self.func("id","layout_departure_time")    #���ʱ���
            #self.func("xpath",u"//android.widget.TextView[@text='����']")                   #ѡ���һ��20��(����һ��Ҫ��u,Ҫ�ӵ���ǰ�����)
            self.func("id","com.wxws.myticket:id/btnQuery")       #�����ѯ
            print u"===����·�б�ҳ�����ǰһ�졢��һ�졿==="
            Initialtime1 = self.func('id',"com.wxws.myticket:id/tvCurDay",get_element="text")
            Initialtime = "".join(re.findall("\d",Initialtime1))    #��ȡʱ������
            self.func("id","com.wxws.myticket:id/tvNextDay")  #�����һ��
            houtime1 = self.func('id',"com.wxws.myticket:id/tvCurDay",get_element="text")
            houtime = "".join(re.findall("\d",houtime1))
            if int(houtime) == (int(Initialtime) + 1): #��ǰ�ȳ�ʼ����
                print(u"�����һ������,���ǰΪ:%s,�㼪��Ϊ:%s"%(Initialtime1,houtime1))

            self.func("id","com.wxws.myticket:id/tvPrevDay")  #���ǰһ��
            houtime3 = self.func('id',"com.wxws.myticket:id/tvCurDay",get_element="text")
            houtime2 = "".join(re.findall("\d",houtime3))
            if (int(houtime)-1) == int(houtime2) :
                print(u"���ǰһ������,���ǰΪ:%s,�����Ϊ:%s"%(houtime1,houtime3))
