'''
Created on 2018-3-28

@author: wuqi2
上线时申请一个公共邮箱.
顾问majing12 账号去开发.

microsoft 先给邮箱 跳转找lenovo的 ADFS页面 邮箱账号密码   如果是外网需要OTP 内网不需要.

'''
from exchangelib import IMPERSONATION,DELEGATE, Account,Credentials,Message, Mailbox, HTMLBody,Q,Configuration,FileAttachment,ItemAttachment

creds = Credentials(
    username='majing12@lenovo.com',  # Or myusername@example.com for O365
    password='Zyam-2520'
)
config = Configuration(server='mail.lenovo.com', credentials=creds)
account = Account(
       primary_smtp_address= 'majing12@lenovo.com', 
       autodiscover=False,
       #credentials=creds,
       config=config,
       access_type=DELEGATE
   )
#print(account.root.tree())
print(account.contacts.tree())
folder = account.root.contacts.test
for p in folder.people():
    print(p)