'''
Created on 2018-3-28

@author: wuqi2
'''
from O365 import *
import time
import logging


Connection.login('wuqi2@lenovo.com', '456rtyRTY222')
#Connection.proxy(url='mail.lenovo.com', port=8080, username='wuqi2@lenovo.com', password='456rtyRTY')
inbox = FluentInbox()
print(inbox)
maillist=inbox.from_folder('Itsmnoreply').search('Subject:Itsmnoreply').fetch(count=5)
print(maillist)

for message in maillist:
    # Just print the message subject
    print(message.getSubject())


#authenticiation = ('wuqi2@lenovo.com','456rtyRTY')
#m = Message(auth=authenticiation)
#m.setRecipients('zhangsm8@lenovo.com')
#m.setSubject('I made an email script.')
#m.setBody('Talk to the computer, cause the human does not want to hear it any more.')
#m.sendMessage()
#print('Done')

#m.fetchAttachments()
#for att in m.attachments:
#    processAttachment(att,resp)

#i = Inbox(auth=authenticiation,getNow=False) #Email, Password, Delay fetching so I can change the filters.
#print(i.message)
#for m in i.messages:
#    print(m)
    
 #   time.sleep(55)
 #   processMessage(m,auth=authenticiation)