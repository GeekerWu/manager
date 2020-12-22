'''
Created on 2019-1-14

@author: wuqi2
'''
import requests
import threading
import time
#import json
#from astropy.io.fits.header import Header
postdata = '''
<REQUESTS ServiceName="LENOVO_TS.CHINA" >
   <REQUEST Name="checkLock" AssignToVar="response" Synchronous="true">
            <SQL_QUERY Value = '123'/>
          </REQUEST>
</REQUESTS>
'''
#url="https://planningm.lenovo.com/sci/bdp/api/chart?form_data=%7B%22datasource%22%3A%227__table%22%2C%22viz_type%22%3A%22bar%22%2C%22groupby%22%3A%5B%22name%22%5D%2C%22metrics%22%3A%5B%22sum__volume%22%5D%2C%22order_by_cols%22%3A%5B%5D%2C%22options%22%3A%7B%22is_stack%22%3Atrue%2C%22legend_pos%22%3A%22left%22%2C%22stack_number_digital%22%3A2%2C%22label_color%22%3A%5B%22%234bc5c3%22%2C%22%235293b8%22%5D%2C%22theme%22%3A%22dark-theme%22%7D%7D"

def process():
#     url="https://planningm.lenovo.com/sci/bdp/api/folders"
#     Header={
#             #'content-type': "application/json",
#             "Authorization":"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDgxMzk2OTYsImVtYWlsIjoid3VxaTJAbGVub3ZvLmNvbSIsInVzZXJuYW1lIjoid3VxaTIiLCJpc3MiOiJwbGFubmluZ20ubGVub3ZvLmNvbSIsInVzZXJfaWQiOjMsIm9yaWdfaWF0IjoxNTQ3MDI0NTU3fQ.s96OlCuO2tSbJ0-B1w0r3zJExAm9Y96xBXnMX2YVXvM"
#             }
# 
# 
#     count=0;
#     while (count < 10):
#         res = requests.get(url,headers=Header)
#         print(res.text)
#         res2 = requests.get(url,headers=Header)
#         print(res2.text)
#         res3 = requests.get(url,headers=Header)
#         print(res3.text)
#         res4 = requests.get(url,headers=Header)
#         print(res4.text)
#         res5 = requests.get(url,headers=Header)
#         print(res5.text)
#         res6 = requests.get(url,headers=Header)
#         print(res6.text)
#         res7 = requests.get(url,headers=Header)
#         print(res7.text)
#         res8 = requests.get(url,headers=Header)
#         print(res8.text)
#         res9 = requests.get(url,headers=Header)
#         print(res9.text)
#         res10 = requests.get(url,headers=Header)
#         print(res10.text)
#         print ('The count is:',count)
#         count=count+1
    #url='https://planningmdev.lenovo.com/auth/api-token-auth/'
    #body={"username":"test","password":"1234test","otpcode":"666666","device_name":"mobile","device_os":"android"}
    url='https://planningm.lenovo.com/auth/api-token-auth/'
    body={"username":"wuqi2","password":"123qweQWE","otpcode":"814807","device_name":"mobile","device_os":"android"}
    
    
    count=0;
    while (count < 10):
        res = requests.post(url,data=body)
        print(res.text)  
        res2 = requests.post(url,data=body)
        print(res2.text)
        res3 = requests.post(url,data=body)
        print(res3.text)
        res4 = requests.post(url,data=body)
        print(res4.text)
        res5 = requests.post(url,data=body)
        print(res5.text)
        res6 = requests.post(url,data=body)
        print(res6.text)
        res7 = requests.post(url,data=body)
        print(res7.text)
        res8 = requests.post(url,data=body)
        print(res8.text)
        res9 = requests.post(url,data=body)
        print(res9.text)
        res10 = requests.post(url,data=body)
        print(res10.text)
        count=count+1
        
    
t0 = threading.Thread(target=process, name='worker0')        
t1 = threading.Thread(target=process, name='worker1')  # 线程对象.
t2 = threading.Thread(target=process, name='worker2')
t3 = threading.Thread(target=process, name='worker3')
t4 = threading.Thread(target=process, name='worker4')
#t5 = threading.Thread(target=process, name='worker5')
#t6 = threading.Thread(target=process, name='worker6')
#t7 = threading.Thread(target=process, name='worker7')
#t8 = threading.Thread(target=process, name='worker8')
#t9 = threading.Thread(target=process, name='worker9')


#def showthreadinfo():
 
#    print('currentthread = {}'.format(threading.current_thread()))
 
#    print('main thread = {}'.format(threading.main_thread()), '"主线程对象"')
 
#    print('active count = {}'.format(threading.active_count()), '"alive"')
 
#showthreadinfo()

t0.start()  # 启动.
t1.start()  # 启动.
t2.start()  # 启动.
t3.start()  # 启动.
t4.start()  # 启动.
# t5.start()  # 启动.
# t6.start()  # 启动.
# t7.start()  # 启动.
# t8.start()  # 启动.
# t9.start()  # 启动.

print('==END==')       