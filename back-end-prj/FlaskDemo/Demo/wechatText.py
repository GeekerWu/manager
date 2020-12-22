'''
Created on 2017-6-12

@author: Administrator
'''
import urllib2
import json
import AccToken
import DBConnect
def Text(soup):
    # <xml><tousername><![CDATA[gh_a14f1a9409ff]]></tousername>
    # <fromusername><![CDATA[oF8Buwo8-nOOERm9Lman4u7tCIAU]]></fromusername>
    # <createtime>1496998837</createtime>
    # <msgtype><![CDATA[text]]></msgtype>
    # <content><![CDATA[helloworld]]></content>
    # <msgid>6429561047487714993</msgid>
    # </xml>
    tousername = soup.tousername.get_text()
    fromusername = soup.fromusername.get_text()
    createtime = soup.createtime.get_text()
    msgtype = soup.msgtype.get_text()
    content = soup.content.get_text()
    msgid = soup.msgid.get_text()
    print content
    #Auto reply user message
    if content == "haha":
        str="<xml>"
        str+="<ToUserName><![CDATA["+fromusername+"]]></ToUserName>"
        str+="<FromUserName><![CDATA["+tousername+"]]></FromUserName>"
        str+="<CreateTime>12345678</CreateTime>"
        str+="<MsgType><![CDATA[text]]></MsgType>"
        str+="<Content><![CDATA[hahahahhahahahahahah]]></Content>"
        str+="</xml>"
    return str     