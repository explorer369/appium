#coding:GBK
import os,sys,time,re,xlrd,util
reload(sys)
sys.setdefaultencoding('GBK')
localpath = os.getcwd()
sys.path.append(localpath)

def open_excel(file= 'file.xls'):
  try:
    data = xlrd.open_workbook(file)
    return data
  except Exception,e:
    print str(e)
#����������ȡExcel����е�����  ����:file��Excel�ļ�·��   colnameindex����ͷ���������е����� ��by_index���������
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
  data = open_excel(file)
  table = data.sheets()[by_index]
  nrows = table.nrows #����
  ncols = table.ncols #����
  colnames = table.row_values(colnameindex) #ĳһ������
  list =[]
  for rownum in range(1,nrows):
    row = table.row_values(rownum)
    if row:
      app = {}
      for i in range(len(colnames)):
        app[colnames[i]] = row[i]
      list.append(app)
  return list