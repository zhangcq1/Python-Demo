# coding:utf-8
import smtplib,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ----------1.跟发件相关的参数------

smtpserver = "smtp.163.com"           # 发件服务器
port = 465                             # 端口
sender = "13781240894@163.com"     # 账号
psw = "EKYBQZDKANDPISHR"                  # 密码
# receiver = ["xxxx@qq.com"]      # 单个接收人也可以是list
# 多个收件人list对象
receiver = [
# "814671584@qq.com",
"1320977331@qq.com",
# "2324604240@qq.com",
# "915818038@qq.com",
# "1647402818@qq.com",
# "3241824790@qq.com",
# "2904388153@qq.com",
# "1049547925@qq.com",
# "jiazhuang0119@qq.com",
# "1223205752@qq.com",
# "shixuan1101@qq.com",
            ]


# ----------2.编辑邮件的内容------
# 读文件
file_path = "result.html"
with open(file_path, "rb") as fp:
    mail_body = fp.read()

msg = MIMEMultipart()
msg["from"] = sender                       # 发件人
msg["to"] = ";".join(receiver)             # 多个收件人list转str
msg["subject"] = "清华录取通知书"              # 主题
#EKYBQZDKANDPISHR
# 正文
body = MIMEText(mail_body, "html", "utf-8")
msg.attach(body)

# 附件
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)

# ----------3.发送邮件------
for ele in receiver:
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)                      # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)# 登录
    time.sleep(8)
    print('y')
    smtp.sendmail(sender, [ele], msg.as_string())  # 发送
    time.sleep(8)
smtp.quit()              