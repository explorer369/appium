 #coding=utf-8

"""

codeManager，自动把本机指定目录下的文件夹打成压缩包，并且作为附件发邮件给指定邮箱，作为备份
2016-06-29 by ruansz

"""

# 解决乱码问题
import sys
reload(sys)
SYS_ENCODING = 'cp936'  # 定义系统编码
sys.setdefaultencoding(SYS_ENCODING)  # 设置默认编码

import email.MIMEBase
import time


# 自定义包导入
from zipManager import zip_manager
from emailManager import email_manager

# 定义一个log函数
def log(msg):
    print time.strftime('%Y-%m-%d %H:%M:%S'), ': ', msg


# run
if __name__ == '__main__':


    log(u'进入run函数')


    log(u'开始读取压缩配置参数')
    # 定义配置参数
    # 1、压缩配置
    timestr = time.strftime('%Y%m%d%H%M%S')   # 生成日期时间字符串，作为压缩文件的版本号
    folder = r'G:\AutoTest\appium\dabao_appium\TestResult'   # 压缩目标文件夹
    target = r'G:\AutoTest\appium\dabao_appium'+timestr+r'.zip'   # 压缩后的名称

    log(u'压缩源文件夹：' + folder)
    log(u'压缩输出路径：' + target)

    log(u'开始生成压缩文件')
    zip_manager.ZipManager.zip_dir(folder, target)
    log(u'生成压缩文件结束')


    log(u'开始读取邮件发送配置参数')
    # 2、发送邮件配置
    mail_cfg = {
        # 邮箱登录设置，使用SMTP登录
        'server_username': 'zhangzhenfei@12308.com',
        'server_pwd': 'Zzf@12',

        # 邮件内容设置（注：请配置smtp_server在email_manager.py）
        'msg_to': ['zzf198987@qq.com', 'zhangzhenfei@12308.com'],  # 可以在此添加收件人
        'msg_subject': u'我的python代码备份1' + timestr,       #标题
        'msg_date': email.Utils.formatdate(),
        'msg_content': u"我的python代码备份" + timestr,        #正文

        # 附件
        'attach_file': target
        }
    log(u'读取邮件发送配置参数：')
    log(u'server_username：' + str(mail_cfg.get('server_username')))
    log(u'server_pwd：' + str(mail_cfg.get('server_pwd')))
    log(u'msg_to：' + str(mail_cfg.get('msg_to')))
    log(u'msg_subject：' + str(mail_cfg.get('msg_subject')))
    log(u'msg_date：' + str(mail_cfg.get('msg_date')))
    log(u'msg_content：' + str(mail_cfg.get('msg_content')))
    log(u'attach_file：' + str(mail_cfg.get('attach_file')))


    # 实例化manager对象
    log(u'开始创建EmailManager')
    email_manager = email_manager.EmailManager(**mail_cfg)
    log(u'开始发送邮件')
    email_manager.run()
    log(u'发送完成')
    log(u'程序结束')