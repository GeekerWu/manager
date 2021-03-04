import os
from exchangelib import IMPERSONATION,DELEGATE, Account,Credentials,Message, Mailbox, HTMLBody,Q,Configuration,FileAttachment,ItemAttachment
def Email(to, subject, body):
    creds = Credentials(
    #username='wuqi2@lenovo.com',  # Or myusername@example.com for O365
    username='odmpsd@lenovo.com',
    #
    

    #password='456rtyRTY'
    password='tofG-2860'
    #tofG-2860
    )
    config = Configuration(server='mail.lenovo.com', credentials=creds)
    account = Account(
        #primary_smtp_address= 'wuqi2@lenovo.com', 
        primary_smtp_address= 'odmpsd@lenovo.com', 
        
        autodiscover=False,
        credentials=creds,
        config=config,
        access_type=DELEGATE
    )
    print(account.root.tree())
    m = Message(
        account=account,
        subject=subject,
        body=HTMLBody(body),
        to_recipients = [Mailbox(email_address=to)]
    )
    #print(account.root.tree())
    #print(account.inbox.total_count)
    #switch attach folder
    curr_folder = account.inbox /'Error folder'
    #get Attachment mails and order by received date desc
    #q = Q(subject='UI Con') & ~Q(subject__startswith='Manual')
    #q = Q(subject__contains=' ')
    #items  = curr_folder.filter(q).order_by('-datetime_received')[:1]
    items  = curr_folder.filter(is_read=True).order_by('-datetime_received')[:2]
    for item in items:
        print(item.subject,item.sender.email_address)
        for attachment in item.attachments:
            if isinstance(attachment, FileAttachment):
                local_path = os.path.join('D:\\tmp', attachment.name)
                with open(local_path, 'wb') as f:
                    f.write(attachment.content)
                #print('Saved attachment to', local_path)
            elif isinstance(attachment, ItemAttachment):
                if isinstance(attachment.item, Message):
                    print(attachment.item.subject, attachment.item.body)
    #print("sending...")
    #m.send()
    print('done!')
print("attachment start...")
Email('wuqi2@lenovo.com', 'Sent from python', 'python python python')


#for item in account.inbox.all().order_by('-datetime_received')[:10]:
#    p‘rint(item.subject, item.body, item.attachments)