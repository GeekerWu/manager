'''
Created on 2018-3-29

@author: wuqi2
'''
from O365 import Inbox
authenticiation = ('finally-weapon@hotmail.com','789uioUIO')
m = Inbox(auth=authenticiation)
print(m)
#m.setRecipients('wuqi2@lenovo.com')
#m.setSubject('I made an email script.')
#m.setBody('Talk to the computer, cause the human does not want to hear it any more.')
#m.sendMessage()