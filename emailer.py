__author__ = 'tryceo'
# Import smtplib for the actual sending function
import smtplib
import configparser

# Import the email modules we'll need
from email.mime.text import MIMEText

config = configparser.ConfigParser()
config.read('logininfo.ini')

sender = config['email']['username']
senderPass = config['email']['password']
senderSmtp = 'smtp-mail.outlook.com'
senderSmtpPort = 587
receiver = ['6145603401@vzwpix.com', 'tryceo@gmail.com']


def sendalert(message):
    msg = MIMEText(message, 'plain')
    msg['Subject'] = 'GPU ALERT'
    msg['From'] = sender
    msg['To'] = ",".join(receiver)

    s = smtplib.SMTP(senderSmtp, senderSmtpPort)
    s.ehlo()
    s.starttls()
    s.login(sender, senderPass)
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()
