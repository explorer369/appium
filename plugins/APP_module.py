# coding=GBK
import os,sys,time,re,xlrd,SettingDevice
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
def huanyingye(self):
    '''1.�󻬴���ӭҳ2.���������ҳ3.�ر����ص���'''
    try:  #�رջ����
        while self.func('xpath',"//android.widget.ImageView[@index='0']",get_element='is_displayed') == True:  #���ж�Ԫ���Ƿ�ɼ���������ּ�����
            #self.func('1000','1000','20','1000',times=500,get_element='swipe',nb=3)   #���󻬶�3��
            SettingDevice.scroll(self,'left',number=3,times=1000)
            self.func('id',"com.wxws.myticket:id/imgOpen")                            #��������
            break                                                                    #ִ�к�����ѭ��
        else:
            time.sleep(0.5)
    except Exception,e:
        pass
    try:  #�ر�����APP����
        time.sleep(3)
        if self.func('ids',"com.wxws.myticket:id/tabView",get_element='is_displayed') == False:   #�Ҳ�����Ʊ��ť˵���е���
            self.driver.keyevent('4')   #�����ؼ�ȡ������
    except Exception,e:
        pass
def init_login(self,i,listdata):
    '''��ҳ������˲��ɹ���¼�󷵻ص���ҳ'''
    for g in range(1,2):
        huanyingye(self)   #����ӭҳ�͵���
        self.func('id',"com.wxws.myticket:id/tvMytext")          #����
        self.func('id',"com.wxws.myticket:id/layout_top_login")  #��¼��ť
        def intstrusername():
            try:
                username = listdata[i]['username']
                username = int(username)
                return username
            except:
                username = listdata[i]['username']
                return username
        def intstrpassword():
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
        self.func('id',"com.wxws.myticket:id/user_name",send_keys='18975428751')
        self.func('id',"com.wxws.myticket:id/pwd",send_keys='881218')
        self.func('id',"com.wxws.myticket:id/login")
        try:
            #self.func('name',u"��ӭ����12308����Ʊ")# �����͵����ȥ��
            #WebDriverWait(self.driver,3).until(lambda x: x.find_element_by_xpath("//*[contains(.,'��ӭ����')]"))
            self.func('ids','com.wxws.myticket:id/tabView')   #�����Ʊ
            break
        except:
            self.driver.keyevent('4')  #���ص���¼ҳ
            continue