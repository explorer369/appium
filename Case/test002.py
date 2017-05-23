import logging,os,sys,time,unittest,xlrd
reload(sys)
sys.setdefaultencoding('GBK')

def open_excel(file= 'file.xls'):
  try:
    data = xlrd.open_workbook(file)
    return data
  except Exception,e:
    print str(e)
#根据索引获取Excel表格中的数据  参数:file：Excel文件路径   colnameindex：表头列名所在行的所以 ，by_index：表的索引
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
  data = open_excel(file)
  table = data.sheets()[by_index]
  nrows = table.nrows #行数
  ncols = table.ncols #列数
  colnames = table.row_values(colnameindex) #某一行数据
  list =[]
  for rownum in range(1,nrows):
    row = table.row_values(rownum)
    if row:
      app = {}
      for i in range(len(colnames)):
        app[colnames[i]] = row[i]
      list.append(app)
  return list
class AndroidTest(unittest.TestCase):
    func = getattr(__import__('find'),'find_name')  #func()# 相当于执行find.py的foo函数
    def setUp(self):
        SettingDevice.Setting_device(self)
    def tearDown(self):
        self.driver.available_ime_engines()  #恢复输入法
        self.driver.close_app()
        self.driver.quit()
    def test12309click(self):
        time.sleep(5)
        listdata = excel_table_byindex('data.xls',0)
        if(len(listdata) <= 0 ):
            assert 0,u"Excel数据库异常"
        for i in range(0,int(len(listdata))):
            print 'Excel中共有：%s 行数据'%(len(listdata))
            time.sleep(6)
            self.func("id","com.wxws.myticket:id/tv_ticket_cjkx",get_element='text')  #点击城际快线
            self.func("id","com.wxws.myticket:id/etBecity")
            self.driver.find_element_by_id('com.wxws.myticket:id/etSearch').send_keys(listdata[i]['username'])
            self.func('class_names','android.widget.TextView',1)
            time.sleep(1)
            #   self.func("id","com.wxws.myticket:id/tv_cancel")
            self.func("id","com.wxws.myticket:id/etEncity")
            self.driver.find_element_by_id('com.wxws.myticket:id/etSearch').send_keys(listdata[i]['password'])
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
            #显示金额详情
            #self.func("id","com.wxws.myticket:id/rl_desc_price")
            #提交订单
           # self.func("id","com.wxws.myticket:id/btnPay")
            #立即支付
            #  self.func("name","    立即支付    ")