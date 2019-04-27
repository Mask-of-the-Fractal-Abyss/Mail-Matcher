import smtplib, ssl
import email
from email.mime.multipart import MIMEMultipart

port = 587
smtp_server = 'smtp.gmail.com'
sender_email = 'XXXXXXXXX'
password = 'XXXXXXXXX'
receiver_email = sender_email
   
def send(msg='helo', subject='', receivers=[], default=True):
    if default:
        subject = 'Mail Matcher: ' + subject
    msg = "Subject: %s\n%s" % (subject, msg)
##    receivers.append(sender_email)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as s:
        s.starttls(context=context)
        s.login(sender_email, password)
        s.sendmail(sender_email, receivers, msg)