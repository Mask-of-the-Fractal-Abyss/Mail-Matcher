import imaplib
from send import *

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(sender_email, password)
mail.list()

def getLatest():
    mail.select('inbox')
    result, data = mail.search(None, 'ALL')

    ids = data[0]
    lst = ids.split()
    
    result, data = mail.fetch(lst[-1], '(RFC822)')
    return data[0][1]

def getLength():
    result, data = mail.search(None, 'ALL')

    ids = data[0]
    lst = ids.split()
    
    return len(lst)

def getString(msg):
    msg = email.message_from_bytes(msg)
    if msg.is_multipart():
        for payload in msg.get_payload():
            return payload.get_payload()
    else:
        return msg.get_payload()
##    if msg.is_multipart():
##        return msg.get_payload()
    return msg.get_payload()

def getSubject(msg):
    return email.message_from_bytes(msg)['subject']

def getAuthor(msg):
    return email.message_from_bytes(msg)['from']