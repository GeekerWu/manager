'''
Created on 2018-3-20

@author: wuqi2
'''
from datetime import timedelta
from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, ServiceAccount, \
    EWSDateTime, EWSTimeZone, Configuration, NTLM, CalendarItem, Message, \
    Mailbox, Attendee, Q, ExtendedProperty, FileAttachment, ItemAttachment, \
    HTMLBody, Build, Version
import os
# Specify your credentials. Username is usually in WINDOMAIN\username format, where WINDOMAIN is
# the name of the Windows Domain your username is connected to, but some servers also
# accept usernames in PrimarySMTPAddress ('myusername@example.com') format (Office365 requires it).
# UPN format is also supported, if your server expects that.
credentials = Credentials(username='\\wuqi2@lenovo.com', password='456rtyRTY')

# If you're running long-running jobs, you may want to enable fault-tolerance. Fault-tolerance
# means that requests to the server do an exponential backoff and sleep for up to a certain
# threshold before giving up, if the server is unavailable or responding with error messages.
# This prevents automated scripts from overwhelming a failing or overloaded server, and hides
# intermittent service outages that often happen in large Exchange installations.

# If you want to enable the fault tolerance, create credentials as a service account instead:
#credentials = ServiceAccount(username='FOO\\bar', password='topsecret')

# An Account is the account on the Exchange server that you want to connect to. This can be
# the account associated with the credentials you connect with, or any other account on the
# server that you have been granted access to.
# 'primary_smtp_address' is the primary SMTP address assigned the account. If you enable
# autodiscover, an alias address will work, too. In this case, 'Account.primary_smtp_address'
# will be set to the primary SMTP address.
my_account = Account(primary_smtp_address='wuqi2@lenovo.com', credentials=credentials,
                     autodiscover=True, access_type=DELEGATE)
#johns_account = Account(primary_smtp_address='john@example.com', credentials=credentials,
#                        autodiscover=True, access_type=DELEGATE)
#marys_account = Account(primary_smtp_address='mary@example.com', credentials=credentials,
#                        autodiscover=True, access_type=DELEGATE)
#still_marys_account = Account(primary_smtp_address='alias_for_mary@example.com',
#                              credentials=credentials, autodiscover=True, access_type=DELEGATE)

# Set up a target account and do an autodiscover lookup to find the target EWS endpoint.
#account = Account(primary_smtp_address='john@example.com', credentials=credentials,
#                  autodiscover=True, access_type=DELEGATE)

# If your credentials have been given impersonation access to the target account, set a
# different 'access_type':
#account = Account(primary_smtp_address='john@example.com', credentials=credentials,
#                  autodiscover=True, access_type=IMPERSONATION)

# If the server doesn't support autodiscover, or you want to avoid the overhead of autodiscover,
# use a Configuration object to set the server location instead:
config = Configuration(server='mail.lenovo.com', credentials=credentials)
#account = Account(primary_smtp_address='john@example.com', config=config,
#                  autodiscover=False, access_type=DELEGATE)

# 'exchangelib' will attempt to guess the server version and authentication method. If you
# have a really bizarre or locked-down installation and the guessing fails, or you want to avoid
# the extra network traffic, you can set the auth method and version explicitly instead:
#version = Version(build=Build(15, 0, 12, 34))
#config = Configuration(server='example.com', credentials=credentials, version=version, auth_type=NTLM)

# If you're connecting to the same account very often, you can cache the autodiscover result for
# later so you can skip the autodiscover lookup:
ews_url = my_account.protocol.service_endpoint
ews_auth_type = my_account.protocol.auth_type
primary_smtp_address = my_account.primary_smtp_address

# 5 minutes later, fetch the cached values and create the account without autodiscovering:
#config = Configuration(service_endpoint=ews_url, credentials=credentials, auth_type=ews_auth_type)
account = Account(
    primary_smtp_address=primary_smtp_address, config=config, autodiscover=False, access_type=DELEGATE
)



# If you need proxy support or custom TLS validation, you can supply a custom 'requests' transport adapter, as
# described in http://docs.python-requests.org/en/master/user/advanced/#transport-adapters
# exchangelib provides a sample adapter which ignores SSL validation errors. Use at own risk.
#from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
#BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

print (account.inbox.total_count)

my_folder = account.inbox

for item in my_folder.all():
    for attachment in item.attachments:
        if isinstance(attachment, FileAttachment):
            local_path = os.path.join('/tmp', attachment.name)
            with open(local_path, 'wb') as f:
                f.write(attachment.content)
            print('Saved attachment to', local_path)
        elif isinstance(attachment, ItemAttachment):
            if isinstance(attachment.item, Message):
                print(attachment.item.subject, attachment.item.body)