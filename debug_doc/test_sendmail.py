# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from sendEmail import SendEmail
from sendEmail import SendHtmlEmail
sendmail=SendEmail.SendEmail('测试发送邮件')
sendmail.sendMail()

#smail=SendHtmlEmail.SendHtmlEmail("D:\\WORK\\AutoTest\\Report")
#smail.send_mail_html()