__author__ = "starry"

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

class send(object):
    # sender
    sender = "2078783415@qq.com"
    # password   hzorxipgmkjsejgb  mbacuqmjjyjybjda   abbdmkinnprddgch   zencbbcbbjzkcjeh   bqawkwheacocbhgc
    pwd = "bqawkwheacocbhgc"
    # reciver user  865725156@qq.com
    reciver = ["starry.feng@nextlabs.com","5345935@qq.com"]
    # email server address
    email_server_address = "smtp.qq.com"
    # item
    title = "Server UI Automation Report"
    content = "hi All \n \t I have finish server spin automation test, this is spin test report, please check it. \n Thanks, \n starry"
    # msg = MIMEText(content,'plain','utf-8')
    msg = MIMEMultipart()
    msg['Subject'] = Header(title, 'utf-8')
    msg['From'] = Header("starry", 'utf-8')
    msg['To'] = Header("feng", 'utf-8')

    def send_to_user(self,file_path):
        try:

            list = file_path.split('/')
            file_name = list[len(list)-1]
            self.msg.attach(MIMEText(self.content, 'plain', 'utf-8'))
            attachment = open(file_path, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
            self.msg.attach(part)

            smtp = smtplib.SMTP_SSL(self.email_server_address, 465)
            smtp.login(self.sender, self.pwd)
            smtp.send_message(self.msg, self.sender, self.reciver)

            smtp.quit()
        except Exception as e:
            print("send email fail")
            print(e)
