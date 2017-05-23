#!/usr/bin/env python
# coding: utf-8

from smtplib import SMTP, quotedata, CRLF, SMTPDataError
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from sys import stderr, stdout
import os,time
import sys
import zip_manager
# 解决乱码问题
import sys
reload(sys)
SYS_ENCODING = 'GB2312'  # 定义系统编码
sys.setdefaultencoding(SYS_ENCODING)  # 设置默认编码

class ExtendedSMTP(SMTP):
  def data(self, msg):
    self.putcmd("data")
    (code,repl)=self.getreply()
    if self.debuglevel > 0 : print >> stderr, "data:", (code, repl)
    if code != 354:
      raise SMTPDataError(code,repl)
    else:
      q = quotedata(msg)
      if q[-2:] != CRLF:
        q = q + CRLF
      q = q + "." + CRLF

      # begin modified send code#开始修改发送代码
      chunk_size = 2048
      bytes_sent = 0

      while bytes_sent != len(q):
        chunk = q[bytes_sent:bytes_sent+chunk_size]
        self.send(chunk)
        bytes_sent += len(chunk)
        if hasattr(self, "callback"):
          self.callback(bytes_sent, len(q))
      # end modified send code

      (code,msg)=self.getreply()
      if self.debuglevel >0 : print>>stderr, "data:", (code,msg)
      return (code,msg)

def callback(progress, total):
  '''发送进度条'''
  percent = 100. * progress / total
  stdout.write('r')
  stdout.write("%s bytes sent of %s [%2.0f%%]" % (progress, total, percent))
  stdout.flush()
  if percent >= 100: stdout.write('n')

def sendmail(subject):
  MAIL_FROM = 'zhangzhenfei@12308.com'   #发送邮件的账号
  MAIL_TO = ['zzf198987@qq.com','zhangzhenfei@12308.com']         #接收邮件账号

  BAK_DIR = u'G:\\AutoTest\\AutoBianli\\appcrawler-1.7.1\\全国汽车票V7.0.6'   #要发送的文件夹，注文件夹下面不能有文件夹
  timestr = time.strftime('%Y%m%d%H%M%S')   # 生成日期时间字符串，作为压缩文件的版本号
  target = u'G:\\AutoTest\\AutoBianli\\appcrawler-1.7.1\\全国汽车票V7.0.6_'+timestr+r'.zip'   # 压缩后的路径和名称
  #压缩文件夹
  zip_manager.ZipManager.zip_dir(BAK_DIR, target)

  msg = MIMEMultipart()
  msg['From'] = MAIL_FROM
  msg['Subject'] = subject

  #正文用text的方式
  text = "Hi!\n全国汽车票V7.0.6版本自动遍历已完成！\n详情请进入以下地址查看完整的详情报告，谢谢！\n \\\\192.168.1.90\\12308\测试文档\TestResult\全国汽车票V7.0.6\n本邮件由系统自动发出！"
  part1 = MIMEText(text, 'plain')
  msg.attach(part1)

  '''
  #正文用HTML的方式
  html = """\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           How are you?<br>
           Here is the <a href="http://www.python.org">link</a> you wanted.
        </p>
      </body>
    </html>
    """
  part2 = MIMEText(html, 'html')
  msg.attach(part2)
  '''

  #遍历目录下的所有文件，注：文件夹不行
  '''
  for filename in os.listdir(BAK_DIR):
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(os.path.join(BAK_DIR, filename),"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filename))
    msg.attach(part)
  '''
  #构造压缩包附件
  att = MIMEText(open(target, 'rb').read(), 'base64', 'gb2312') #设置附件的目录
  att["Content-Type"] = 'application/octet-stream'
  #截取保存的压缩包文件名u
  AttachmentName = target.split("\\")[-1]    #G:\AutoTest\appium\autoAPPiumGBKdabao20170213172802.zip
  att["Content-Disposition"] = 'attachment; filename="%s"'%AttachmentName  #设置附件的名称
  #msg.attach(att)

  #构造截图附件
  att1 = MIMEText(open(u'G:\\AutoTest\\AutoBianli\\appcrawler-1.7.1\\全国汽车票V7.0.6\\111.jpg', 'rb').read(), 'base64', 'gb2312') #设置附件的目录
  att1["Content-Type"] = 'application/octet-stream'
  att1["Content-Disposition"] = 'attachment; filename=u"报告截图.jpg"'  #设置附件的名称
  att1["Accept-Language"]="zh-CN"
  att1["Accept-Charset"]="ISO-8859-1,gb2312"
  msg.attach(att1)


  try:
    smtp = ExtendedSMTP()
    smtp.callback = callback
    smtp.connect(r'smtp.exmail.qq.com', 25)
    smtp.login('zhangzhenfei@12308.com', 'Zzf@12')
    smtp.sendmail(MAIL_FROM, MAIL_TO, msg.as_string())
    smtp.close()
    #os.system('rm -f %s/*' % BAK_DIR)
  except Exception, e:
    print e

if __name__ == '__main__':
  sendmail('全国汽车票V7.0.6版本自动遍历测试报告')  #调式时用
  '''用法send_files '邮件标题'''
  '''
  if len(sys.argv) == 1:
    print 'Please specific a subject'
    print 'Usage: send_files '
  else:
    sendmail(sys.argv[1])
  '''