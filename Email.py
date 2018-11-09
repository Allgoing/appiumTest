import smtplib
import traceback
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class EMail:

    # smtp_addr: 邮件服务器
    # from_addr: 发送人地址
    # from_pwd: 邮件授权码
    # to_addrs: 接收人地址
    # file_path: 附件地址
    # mail_title: 邮件标题
    # to_addrs_cc: 抄送人地址
    def __init__(self, smtp_addr='smtp.qq.com', from_addr='3162909642@qq.com', from_pwd='hdvnaxyzhdcmddca'):
        self._smtp_addr = smtp_addr
        self._from_addr = from_addr
        self._from_pwd = from_pwd

    def send_mail(self, mail_title, to_addrs_in='573447533@qq.com', file_path=None, to_addrs_cc=None, content=None,
                  image_body=None, image=None):
        """设置邮件头"""
        msg = MIMEMultipart('related')
        msg['Subject'] = mail_title
        msg['From'] = self._from_addr
        msg['To'] = to_addrs_in
        msg['Cc'] = to_addrs_cc
        msg.attach(MIMEText(image_body, 'html', 'utf-8'))

        if image_body:
            # 二进制模式读取图片
            with open(image, 'rb') as f:
                msgImage = MIMEImage(f.read())
            # 定义图片ID
            msgImage.add_header('Content-ID', '<image1>')
            msg.attach(msgImage)

        if file_path:
            with open(file_path, 'rb') as fp:
                '''添加附件'''
                try:
                    fp_part = MIMEApplication(fp.read())
                    fp_part.add_header('Content-Disposition', 'attachment', filename='index.html')
                    fp_part.add_header('Content-ID', '<0>')
                    fp_part.add_header('X-Attachment-Id', '0')
                    msg.attach(fp_part)
                except Exception:
                    print('文件不存在')
                    print(traceback.print_exc())

        try:
            server = smtplib.SMTP_SSL(self._smtp_addr, 465)
            # server.set_debuglevel(1)
            server.login(self._from_addr, self._from_pwd)
            if to_addrs_cc is None:
                server.sendmail(self._from_addr, to_addrs_in.split(','), msg.as_string())
            else:
                server.sendmail(self._from_addr, (to_addrs_in + ',' + to_addrs_cc).split(','), msg.as_string())
            server.quit()
        except Exception:
            print("邮件发送失败")
            print(traceback.print_exc())


if __name__ == '__main__':
    a = EMail()
    a.send_mail('111', file_path=r'/Users/user/Documents/abc.html', content='wojiushi')
