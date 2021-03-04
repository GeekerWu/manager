'''
Created on 2019-8-7

SDC_tst   300GB , 
"host":10.96.112.200:8080

"user": " SDC_tst ",
"access_key": " 9NEW0GH29TPMVQSORNFE ",
"secret_key": "apCLGDk80vMAd3bEDb0aP0QL1JGeSN1qDO638r0Q"



@author: wuqi2
'''
import boto
import boto.s3.connection
access_key = '9NEW0GH29TPMVQSORNFE'
secret_key = 'apCLGDk80vMAd3bEDb0aP0QL1JGeSN1qDO638r0Q'

conn = boto.connect_s3(
aws_access_key_id = access_key,
aws_secret_access_key = secret_key,
host = "10.96.112.200:8080",
#is_secure=False,               # uncomment if you are not using ssl
calling_format = boto.s3.connection.OrdinaryCallingFormat()
)

bucket = conn.create_bucket('tester666')

for bucket in conn.get_all_buckets():
    print(bucket)
        
conn.delete_bucket(bucket.name)

print('done')

