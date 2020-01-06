import smtplib
from email.mime.text import MIMEText
from email.header import Header
mail_host="smtp.163.com"
mail_user="18221278570"
mail_pass="loveyadan0312"

sender = '18221278570@163.com'
receivers = ['libozhang@microport.com']  # 接收邮件，
 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('it is first email sent by py...', 'plain', 'utf-8')
message['From'] = Header("18221278570@163.com", 'utf-8')     # 发送者
message['To'] =  Header('libozhang@microport.com')          # 接收者
 
subject = 'just test'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
