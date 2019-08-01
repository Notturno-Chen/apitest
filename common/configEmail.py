import smtplib
import getpathInfo
import os
import datetime
from readConfig import readConfig
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email.header import Header

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr), 'utf-8')

# 发件人邮箱和密码
from_addr = readConfig().get_email('from_address')
password = readConfig().get_email('password')
# 收件人邮箱地址
to_addr = readConfig().get_email('to_address')
# 抄送人邮箱地址，后续再加
# to_cc = readConfig().get_email('cc')
# to_bcc = readConfig().get_email('bcc')
# smtp服务器地址和端口
smtp_server = readConfig().get_email('mail_server')
stmp_port = readConfig().get_email('mail_port')

def create_mail():
    # 创建邮件对象
    msg = MIMEMultipart()
    mail_subject = readConfig().get_email("subject")
    subject = str(datetime.datetime.now())[0:19] + ' %s' % mail_subject
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = _format_addr('发件人<%s>' % from_addr)
    msg['To'] = _format_addr('收件人<%s>' % to_addr)

    # 邮件正文是MIMEText
    mail_content = 'This is a Test_Report email, please open attachment file to get more details!'
    msg.attach(MIMEText(mail_content, 'html', 'utf-8'))  # 要调整
    # 构造附件，传送该路径下的文件并打开
    path_info = getpathInfo.get_Path()
    attach_path = os.path.join(path_info, 'result', 'report.html')
    mime = MIMEText(open(attach_path, 'rb').read(), 'base64', 'utf-8')
    # 加上必要的头信息,filename为邮件中的附件名称
    mime.add_header('Content-Disposition', 'attachment', filename='report.html')
    # 给附件编号，可用于正文显示附件内容
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 添加到MIMEMultipart
    msg.attach(mime)
    return msg

def send_mail():
    try:
        server = smtplib.SMTP_SSL(smtp_server, stmp_port)
        # 打印出与smtp服务器交互的所有信息
        # server.set_debuglevel(1)
        # 登录smtp服务器
        server.login(from_addr, password)
        # 发邮件，可以发给多个人，所以传入list。邮件正文是str，as_string将MIMEText转为str
        message = create_mail()
        server.sendmail(from_addr, [to_addr], message.as_string())
        print('Send successfully!')
        # 关闭smtp对话
        server.quit()
    except smtplib.SMTPException as e:
        print('Send failed!')
        print(e)

if __name__ == '__main__':
    send_mail()
