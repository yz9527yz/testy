# -- coding: utf-8 --
import smtplib  # 发送邮件模板
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header  # 定义邮件标题
from email.mime.multipart import MIMEMultipart  # 用于传送附件
from redmine.Common.log import logger


class SendSmptEmail():
    def send_email(latest_report):
        # 读取最新测试报告的内容
        with open(latest_report,'rb') as e:
            mail_content=e.read()
            e.close()

            smtpserver = 'smtp.qq.com'  # 发送邮件所用的服务器
            password = 'lqhxhlvuvajpdiaj'

            # 发送邮件地址和接收地址
            sender = '1807822529@qq.com'

            receives = ['1105425513@qq.com', ]

            # 定义邮件标题和内容
            subject = 'Redmine后台自动化测试报告'

            msgRoot = MIMEMultipart()
            msgRoot['Subject'] = Header(subject, 'utf-8')  # 标题类型
            msgRoot['From'] = sender
            msgRoot['To'] = ','.join(receives)

            # 发送附件
            att = MIMEText(mail_content, "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename="Redmine_report.html"'  # 定义附件名称
            msgRoot.attach(att)  # 挂起
            smtp = smtplib.SMTP_SSL(smtpserver, 465)  # SSL协议端口号要使用465或994
            smtp.helo(smtpserver)  # HELO向服务器标志用户身份
            smtp.ehlo(smtpserver)  # 服务器返回结果确认
            smtp.login(sender, password)
            logger.info('start send Email...')
            smtp.sendmail(sender, receives, msgRoot.as_string())  # 发送地址；邮件接收地址；发送信息
            smtp.quit()
            logger.info('send end...')



