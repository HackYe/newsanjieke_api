# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/8/7 14:54
"""

import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

username = 'yuanye@sanjieke.com'
password = "4zJtsEaEYXxk7CGL"
sender = username
receivers = ','.join(['3004@sina.com'])


def email(report):
    # 设置请求头信息
    msg = MIMEMultipart()
    msg['Subject'] = '三节课app接口测试报告'  # 邮件名
    msg['From'] = sender
    msg['To'] = receivers

    jpgpart = MIMEApplication(open(report, 'rb').read())
    jpgpart.add_header('Content-Disposition', 'attachment', filename='Sanjieke_Auto_Api.html')
    msg.attach(jpgpart)
    msg.attach(MIMEText('这是三节课app接口的测试报告，请查收！'))

    # 发送邮件
    client = smtplib.SMTP()
    client.connect('smtp.exmail.qq.com')
    client.login(username, password)
    client.sendmail(sender, receivers, msg.as_string())
    client.quit()
    print("邮件发送成功，请查看")


if __name__ == '__main__':
    data = '../Outputs/html/Report_2020-08-07-10-09-12.html'
    email(data)
