'''
Created on Sep 16, 2018

@author: Li Xing
'''
import smtplib
from email.mime.text import MIMEText
#设置服务器所需信息
#163邮箱服务器地址
mail_host = 'smtp.163.com'
#163用户名
mail_user = 'lixingsteven@163.com'
#密码(部分邮箱为授权码) 
mail_pass = 'lx123456'
#邮件发送方邮箱地址
sender = 'lixingsteven@163.com'  
#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['984640740@qq.com']  

#设置email信息
#邮件内容设置
message = MIMEText('content','plain','utf-8')
#邮件主题       
message['Subject'] = 'title' 
#发送方信息
message['From'] = sender 
#接受方信息     
message['To'] = receivers[0]  

#登录并发送邮件
try:
    smtpObj = smtplib.SMTP_SSL(mail_host)
    #登录到服务器
    smtpObj.login(mail_user,mail_pass) 
    #发送
    smtpObj.sendmail(
        sender,receivers,message.as_string()) 
    #退出
    smtpObj.quit() 
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误