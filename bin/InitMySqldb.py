# -*- coding:utf-8 -*-
import requests, xlrd, MySQLdb, time, sys
from ConfigParser import ConfigParser
def config():
    configfile='config.txt' 
    config=ConfigParser()
    config.read(configfile)
    host = config.get('database','host')
    port = int(config.get('database','port'))
    db = config.get('database','dbname')
    user = config.get('database','user')
    passwd = config.get('database','password')
    charset = config.get('database','charset')
    return host,port,db,user,passwd,charset
def MySqldb(self,sql):
    host,port,db,user,passwd,charset = config()
    sql = sql
    coon = MySQLdb.connect(user=user,passwd=passwd,db=db,port=port,host=host,charset=charset)
    cursor = coon.cursor()
    return cursor.execute(sql)
    coon.commit()
    cursor.close()
    coon.close()