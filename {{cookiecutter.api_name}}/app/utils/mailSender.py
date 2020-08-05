import smtplib, ssl
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class mailSender:
    def __init__(self, config):
        self.loadConfig(config)
        self.subject = ''
        self.body = MIMEText('',"html")
        self.recipients = []
        self.attachment = None
        self.mail = MIMEMultipart("alternative")

    def setSubject(self,subject):
        self.subject = subject
    
    def setBody(self,body):
        self.body = MIMEText(body,"html")

    def setRecipients(self, recipients:list):
        self.recipients = recipients

    def setAttachment(self, attachment, filename):
        self.attachment = attachment
        self.attName = filename

    def loadConfig(self, config):
        self.config = config

    def sendEmail(self, recipient = None):
        self.mail["From"] = 'KOFRE'
        self.mail["Subject"] = self.subject
        self.mail.attach(self.body)
        if self.attachment != None:
            sheet = MIMEBase('application', 'octet-stream')
            sheet.set_payload(self.attachment)
            encoders.encode_base64(sheet)
            sheet.add_header('Content-Disposition',"attachment", filename=self.attName)
            self.mail.attach(sheet)
        with smtplib.SMTP(self.config["server"],
                          self.config["port"]) as server:
            server.starttls()
            server.login(self.config["user"], self.config["pass"])
            if recipient == None:
                for rec in self.recipients:
                    self.mail["To"] = rec["addr"]
                    server.sendmail('noreply',
                                    rec["addr"],
                                    self.mail.as_string())
            else:
                self.mail["To"] = recipient
                server.sendmail('noreply',
                                recipient,
                                self.mail.as_string())

