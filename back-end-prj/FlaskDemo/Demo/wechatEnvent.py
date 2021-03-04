'''
Created on 2017-6-12

@author: wuqi2
'''
import urllib2
import json
import AccToken
import DBConnect

def event(soup):
#     event inster log to WX_USR_EVENT
    tousername=soup.tousername.get_text()
    fromusername=soup.fromusername.get_text()
    createtime=str(soup.createtime.get_text())
    msgtype=soup.msgtype.get_text()
    event=soup.event.get_text()
#     eventkey=soup.eventkey.get_text()
    sql = "INSERT INTO WX_USR_EVENT (TOUSERNAME,FROMUSERNAME,CREATETIME,MSGTYPE,EVENT) VALUES ('"+tousername+"','"+fromusername+"','"+createtime+"','"+msgtype+"','"+event+"')"
    DBConnect.dbModify(sql)
def subscribe(openid):
    #500000/day  getuser_info('oF8BuwgGuoo5mI_hGhxuKXYd61eA')  WX_USR_INFO
    acc_token=AccToken.getAccToken('wx3418d0ea923e2cab', 'a6484ab5228fe16548078852a442838f')
    url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token="+acc_token+"&openid="+openid+"&lang=zh_CN"
    req = urllib2.Request(url)
    #print req 
    # {
    #    "subscribe": 1, 
    #    "openid": "o6_bmjrPTlm6_2sgVt7hMZOPfL2M", 
    #    "nickname": "Band", 
    #    "sex": 1, 
    #    "language": "zh_CN", 
    #    "city": "guangzhou", 
    #    "province": "guangdong", 
    #    "country": "china", 
    #    "headimgurl":  "http://wx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4
    # eMsv84eavHiaiceqxibJxCfHe/0",
    #   "subscribe_time": 1382694957,
    #   "unionid": " o6_bmasdasdsad6_2sgVt7hMZOPfL"
    #   "remark": "",
    #   "groupid": 0,
    #   "tagid_list":[128,2]
    # }
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    res = json.loads(res)  
    print res
    openid =res.get('openid')
    print 'openid',openid
    nickname = res.get('nickname')
    print 'nickname',nickname
    sex=str(res.get('sex'))
    print 'sex',sex
    try:
        lang=str(res.get('language'))
    except:
        lang='X'
    print 'lang',lang
    try:
        city=str(res.get('city'))
    except:
        city='X'
    print 'city',city 
    try:
        province =str(res.get('province'))
    except:
        province ='X'
    print 'province',province
    try:
        country =res.get('country')
    except:
        country ='X'
    print 'country',country
    subscribe_time = str(res.get('subscribe_time'))
    print 'subscribe_time',subscribe_time
#             print 'AccessToken :',res['access_token']
#         if res.get('expires_in')!=None:
#             print 'expires :',res['expires_in']
    sql = "INSERT INTO WX_USR_INFO (openid,nickname,sex,lang,city,province,country,subscribe_time) VALUES ('"+openid+"','"+nickname+"','"+sex+"','"+lang+"','"+city+"','"+province+"','"+country+"','"+subscribe_time+"')"
#     print sql
    DBConnect.dbModify(sql)
    return nickname

   
# print getuser_info('oF8Buwo8-nOOERm9Lman4u7tCIAU')