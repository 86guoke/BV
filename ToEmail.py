#__author__ = 'user'
#coding: utf-8
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
msg=MIMEMultipart('related')
'''''
最后终于还是找到解决办法了：邮件主题为‘test’的时候就会出现错误，换成其他词就好了。。我也不知道这是什么奇葩的原因
'''
msg['Subject'] = u'bv 自动化报告'
msg['From'] = '18355356673@163.com'
msg['To'] = "1059966289@qq.com"
content = "hello world"
txt = MIMEText(content)
msg.attach(txt)




def sendmail(name):
    #构造附件
    att = MIMEText(open('Report\\%s.html'%name, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s.html"'%name
    msg.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login('18355356673@163.com', 'hjg123456')
        smtp.sendmail('18355356673@163.com', '1059966289@qq.com', msg.as_string())
        smtp.quit()
        print u'邮件发送成功email has send out !'
    except Exception,e:
        print u"失败"+str(e)

if __name__ == "__main__":
    sendmail("20170427142448")

