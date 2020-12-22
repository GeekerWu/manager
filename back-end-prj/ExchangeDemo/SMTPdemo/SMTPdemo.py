'''
Created on 2019-7-10
@author: wuqi2
'''
#pip install PyEmail
# import numpy as np
# import pandas as pd
import os
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import random

def loadList(infile):
    f=open(infile,'r')
    sourceInLine=f.readlines()
    dataset=[]
    for line in sourceInLine:
        temp1=line.strip('\n')
        temp2=temp1.split('\t')
        dataset.append(temp2)
    return dataset
#file path
infile='D:\\Users\\wuqi2\\Desktop\\tester.txt'
# D:\\Users\\wuqi2\\Desktop\\tester.txt
infile=loadList(infile)
#print(infile)
for address in infile[0]:
    print(address)
    t=random.randrange(2,4)
    print(t)
    time.sleep(t)
    to_list=['wuqi2@lenovo.com']
    sender_mail = 'Nordken@outlook.com'
    account='Nordken@outlook.com'
    pwd='Dk123456'
    mail_host = 'smtp.office365.com'
    mail_port =587
    message = MIMEMultipart()
    message['From'] = sender_mail
    message['To'] = ";".join(to_list)
    subject = "mail subject"
    message['Subject'] = Header(subject)
    #mail content
    body = """
           tester 
    """
    # if has attachments
    message.attach(MIMEText(body, 'plain', 'utf-8'))
    #excel_path = "/root/"
    #name = "xxxx.xlsx"
    #path_name = os.path.join(excel_path, name)
    try:
        #attfile = MIMEText(open(path_name, 'rb').read(), 'plain', 'utf-8')
        #attfile["Content-Disposition"] = 'attachment; filename='+name
        #message.attach(attfile)
        stmtp_obj = smtplib.SMTP(mail_host,mail_port)
        stmtp_obj.starttls()
        stmtp_obj.set_debuglevel(1)
        stmtp_obj.login(account, pwd)
        stmtp_obj.sendmail(sender_mail, address, message.as_string())
    except Exception as e:
        print(str(e))
        print(address)
        print("send failed！")
    else:
        print("send successed！")