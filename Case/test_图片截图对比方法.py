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
        self.extend = extend.Appium_Extend(self.driver)      #����extend�ļ��µ�Appium_Extend��
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
        print u"========����������ҳ�Ż�ȯ��============="
        if(len(listdata) <= 0 ):
            assert 0,u"Excel���ݿ��쳣"
        for i in range(0,int(len(listdata))):
            print 'Excel�й��У�%s ������'%(len(listdata))
            #APP_InitLogin.init_login(self,i,listdata)      #�����򵼺͵�¼
            SettingDevice.scroll(self,'left',number=3,times=1000)  #���ϻ�����Ļ
            SettingDevice.get_element_screen(self,"id","com.wxws.myticket:id/etBecity",name="fff")  #��ͼ�ؼ�ͼƬ
            #SettingDevice.test_same_as(self,"id","com.wxws.myticket:id/etBecity")  #�ؿؼ�ͼΪ���汣��ĶԱ�
            self.func("id","com.wxws.myticket:id/etBecity")  #������
            self.func('id',"com.wxws.myticket:id/etSearch",send_keys=listdata_chengshi[i]['username'])
            self.func('class_names','android.widget.TextView',1)   #ѡ���һ��
            self.func("id","com.wxws.myticket:id/etEncity")        #�������
            self.func('class_names','android.widget.TextView',1)   #ѡ���һ��

            self.func('id',"com.wxws.myticket:id/etSearch",send_keys=listdata_chengshi[i]['password'])
            self.func('class_names','android.widget.TextView',1)  #ѡ���һ��
            SettingDevice.test_same_as(self,"id","com.wxws.myticket:id/etEncity",percent=1)
            '''
            #self.func("id","layout_departure_time")    #���ʱ���
            #self.func("xpath",u"//android.widget.TextView[@text='����']")                   #ѡ���һ��20��(����һ��Ҫ��u,Ҫ�ӵ���ǰ�����)
            self.func("id","com.wxws.myticket:id/btnQuery")       #�����ѯ
            self.func('class_names','android.widget.LinearLayout',number=2)    #�����·�б��еĵڶ�����·
            self.func("xpath",u"//android.widget.TextView[@text='ƱԴ����']")  #���ƱԴ����İ��
            self.func("id","com.wxws.myticket:id/layoutQuan")   #�Ż�ȯ
            if SettingDevice.find_toast(self,By.XPATH,u".//*[contains(@text,'û�п�ʹ�õ��Ż�ȯ')]") :
                print u"��ǰ�˺�û�п��õ��Ż�ȯ"
            else:
                print u"�п��õ��Ż�ȯ"
            '''