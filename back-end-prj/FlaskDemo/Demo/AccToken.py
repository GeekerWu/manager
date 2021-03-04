'''
Created on 2017-6-9
@author: wuqi
'''
# appid='wx3418d0ea923e2cab'
# appsecret='a6484ab5228fe16548078852a442838f'

import DBConnect
import time
from time import sleep
import urllib2
import urllib
import json
def getAccToken(appid,appsecret):
    sql="SELECT RefreshTime FROM WX_Access_Token WHERE appid='"+appid+"'"
#     print sql
    result = DBConnect.dbSelect(sql)
    for item in result:
        RefreshTime=item[0]
#         print item[0]    
    TimeoutTime =  int(RefreshTime) + 7200
    CurrentTime=int(time.time())
    if CurrentTime>= TimeoutTime:
        #print 'AccToken TimeOut ,Get New  Acctoken'  2000/Day   
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="+appid+"&secret="+appsecret
        req = urllib2.Request(url)
    #     print req 
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        res = json.loads(res)  
    #     print res
        if res.get('access_token')!=None:
            access_token=res['access_token']
#             print 'AccessToken :',res['access_token']
#         if res.get('expires_in')!=None:
#             print 'expires :',res['expires_in']
        if res.get('errcode')!=None:
            print res['errcode'],res['errmsg']
#       print 'SystemTime:',int(time.time())
        CurrentTime=int(time.time())
    #     sleep(5)
    #     print 'SystemTim5:',int(time.time())
        sql = "UPDATE WX_Access_Token SET access_token = '"+access_token+"' , RefreshTime = '"+str(CurrentTime)+"' WHERE appid = '"+appid+"'"
#         print sql
        res = DBConnect.updateAccToken(sql)
#         print 'New AccToken:',access_token
        return access_token
    else:
#         print 'Get AccToken from DB'
        sql="SELECT ACCESS_TOKEN FROM WX_Access_Token WHERE appid='"+appid+"'"
#         print sql
        result = DBConnect.dbSelect(sql)
        for item in result:
            Access_Token=item[0]
#         print Access_Token   
        return Access_Token


#print 'get AccToken',getAccToken('wx3418d0ea923e2cab','a6484ab5228fe16548078852a442838f')