#_*_coding:GBK
import ntplib,os,datetime,time
from pickle import FALSE
from xlrd.formula import rangename2d

def EffectiveTime():
    '''������֤��������
    '''
    # ���ù������ڣ�ע���ʽҪһ�£�
    ExpirationTime = 1507593600 #2017-10-10
    #ExpirationTime = 1307593600
    print '��֤�У���ȴ�...'
    #��ȡ����ʱ��
    c = ntplib.NTPClient()
    if ExpirationTime != 0:
        try:
            response = c.request('time-nw.nist.gov')
            NetworkTime = int(response.tx_time)
            if ExpirationTime > NetworkTime:
                NetworkTime = 'qqq'
                return True
            else:
                return False
        except Exception,e:
            NetworkTime = 'qqq'

    if NetworkTime == 'qqq':
        try:
            response = c.request('time.nist.gov')
            NetworkTime = int(response.tx_time)
            if ExpirationTime > NetworkTime:
                NetworkTime = 'qqq'
                return True
            else:
                return False
        except Exception,e:
            NetworkTime = 'qqq'

    if NetworkTime == 'qqq':
        try:
            response = c.request('pool.ntp.org')
            NetworkTime = int(response.tx_time)
            if ExpirationTime > NetworkTime:
                NetworkTime = 'qqq'
                return True
            else:
                return False
        except Exception,e:
            pass
    if NetworkTime == 'qqq':
        try:
            response = c.request('time-a.nist.gov')
            NetworkTime = int(response.tx_time)
            if ExpirationTime > NetworkTime:
                NetworkTime = 'qqq'
                return True
            else:
                return False
        except Exception,e:
            pass
    if NetworkTime == 'qqq':
        try:
            response = c.request('time-b.nist.gov')
            NetworkTime = int(response.tx_time)
            if ExpirationTime > NetworkTime:
                NetworkTime = 'qqq'
                return True
            else:
                return False
        except Exception,e:
            pass
    if NetworkTime == 'qqq':
        try:
            response = c.request('time.windows.com')
            NetworkTime = int(response.tx_time)
            if ExpirationTime > NetworkTime:
                NetworkTime = 'qqq'
                return True
            else:
                return False
        except Exception,e:
            print '�ѹ��ڻ���������ʧ�ܣ������ԣ�'



def EffectiveTime1():
    '''������֤��������
    '''
    # ���ù������ڣ�ע���ʽҪһ�£�
    ExpirationTime = '2017-10-10'
    ExpirationTime = time.strptime(ExpirationTime,'%Y-%m-%d') #תΪ<type 'time.struct_time'>���͵ĸ�ʽ
    #��ȡ����ʱ��
    c = ntplib.NTPClient()
    try:
        response = c.request('time-nw.nist.gov')
        ts = response.tx_time
        _date = time.strftime('%Y-%m-%d',time.localtime(ts)) #�����2016-07-10
        _time = time.strftime('%X',time.localtime(ts))      #�����13:14:26
        NetworkTime = time.strptime(_date,'%Y-%m-%d')  #��ȡ��ʱ��ΪstrתΪ<type 'time.struct_time'>
    except Exception,e:
        response = c.request('time.nist.gov')
        ts = response.tx_time
        _date = time.strftime('%Y-%m-%d',time.localtime(ts)) #�����2016-07-10
        _time = time.strftime('%X',time.localtime(ts))      #�����13:14:26
        NetworkTime = time.strptime(_date,'%Y-%m-%d')
    except Exception,e:
        response = c.request('pool.ntp.org')
        ts = response.tx_time
        _date = time.strftime('%Y-%m-%d',time.localtime(ts)) #�����2016-07-10
        _time = time.strftime('%X',time.localtime(ts))      #�����13:14:26
        NetworkTime = time.strptime(_date,'%Y-%m-%d')
    except Exception,e:
        response = c.request('time-a.nist.gov')
        ts = response.tx_time
        _date = time.strftime('%Y-%m-%d',time.localtime(ts)) #�����2016-07-10
        _time = time.strftime('%X',time.localtime(ts))      #�����13:14:26
        NetworkTime = time.strptime(_date,'%Y-%m-%d')
    except Exception,e:
        response = c.request('time-b.nist.gov')
        ts = response.tx_time
        _date = time.strftime('%Y-%m-%d',time.localtime(ts)) #�����2016-07-10
        _time = time.strftime('%X',time.localtime(ts))      #�����13:14:26
        NetworkTime = time.strptime(_date,'%Y-%m-%d')
    except Exception,e:
        response = c.request('time.windows.com')
        ts = response.tx_time
        _date = time.strftime('%Y-%m-%d',time.localtime(ts)) #�����2016-07-10
        _time = time.strftime('%X',time.localtime(ts))      #�����13:14:26
        NetworkTime = time.strptime(_date,'%Y-%m-%d')
    #��ȡ����ϵͳʱ��
    SystemTime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    SystemTime = time.strptime(SystemTime,'%Y-%m-%d')
    try:
        if ExpirationTime > NetworkTime:
            return True
        else:
            print '��֤���ڣ�����ϵ���ߣ�'
            return False
    except (UnboundLocalError,Exception) as e:
        print e,'\n��֤���ڣ�����ϵ���ߣ���������������ԣ�'
        return False
def getdays(days,Format):
  #  getdays(0,'%Y-%m-%d')
    now=datetime.datetime.now()
    delta=datetime.timedelta(days)
    n_days=now+delta
    return n_days.strftime(Format)