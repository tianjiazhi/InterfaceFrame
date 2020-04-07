# coding = utf-8
"""
@Time      : 2020/2/29 0029 11:41
@Author    : YunFan
@File      : send_email.py
@Software  : PyCharm
@Version   : 1.0
@Description: 
"""

# Python中支持的邮件发送的模块
import smtplib
# 用来构造邮件文本的模块
from email.mime.text import MIMEText
# 用来构造邮件中包含附件模块
from email.mime.multipart import MIMEMultipart
# 用来构造邮件头模块
from email.header import Header
# 导入读取配置文件的模块
from data.get_config_data import ReadConfig


class SendEmail:
    def __init__(self):
        read_conf = ReadConfig()
        # 获取发送邮件的服务器
        self.email_server = read_conf.get_email_config_var('email_server')
        # 获取授权码
        self.authorization_code = read_conf.get_email_config_var('authorization_code')

        # 获取发件人的邮件地址
        self.sender = read_conf.get_email_config_var('sender')
        # 获取收件人的邮件地址，有多个时中间使用“;”进行分割
        self.receivers = read_conf.get_email_config_var('receivers')
        # 获取抄送者的邮件地址,有多个时中间使用“;”进行分割
        self.copy_user = read_conf.get_email_config_var('copy_user')

        # 获取邮件主题
        self.subject = read_conf.get_email_config_var('subject')
        # 邮件正文
        self.content = read_conf.get_email_config_var('content')
        # 附件昵称
        self.attachment_nickname = read_conf.get_email_config_var('attachment_nicknames')



    def send_email(self,pass_list:list,fail_list:list,attachment_name:str):
        """
        填写定义邮件内容，并发送邮件
        :param attachment_names: 附件的相对路径和名称 ['写完excel文件的路径和名称','log文件路径及名称']
        :param content_var: 正文中缺少的变量  ['运行总数','通过数','失败数','通过率','失败率']
        :return:
        """
        message = MIMEMultipart('related')
        # 给带附件的邮件添加属性“邮件主题”
        message['Subject'] = Header(self.subject, 'utf-8')

        # 给带附件的邮件添加属性“发送人”
        sender = "云帆" + "<" + self.sender + ">"
        message['From'] = Header(sender, 'utf-8')

        # 给带附件的邮件添加属性“接收人”
        message['To'] = Header(self.receivers, 'utf-8')

        # 给带附件的邮件添加属性“抄送人”
        message['Cc'] = Header(self.copy_user,'utf-8')

        # 邮件正文
        pass_num = len(pass_list)
        fail_num = len(fail_list)
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" %(pass_num/count_num*100)
        fail_result = "%.2f%%" %(fail_num/count_num*100)

        content = self.content.format(count_num,pass_num,fail_num,pass_result,fail_result)
        message.attach(MIMEText(content,'plain', 'utf-8'))

        # 构造附件
        try:
            att1 = MIMEText(open(attachment_name, 'rb').read(), 'base64', 'utf-8')
        except Exception:
            print("发送的附件文件未找到")
        else:
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename=' + self.attachment_nickname
            message.attach(att1)

        try:
            # 创建一个邮件服务器属性
            myMailServer = smtplib.SMTP(self.email_server, 25)
            # 登录邮件服务器
            myMailServer.login(self.sender, self.authorization_code)
            # 发送邮件
            receivers_list = self.receivers.split(";")
            copy_user_list = self.copy_user.split(";")
            myMailServer.sendmail(self.sender,[receivers_list]+[copy_user_list] ,message.as_string())
            # 退出邮件服务器
            myMailServer.quit()
        except smtplib.SMTPException:
            print("邮件通过邮件服务器发送失败")


if __name__ == "__main__":
    # SendEmail().send_email()
    pass

