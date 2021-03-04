'''
Created on 2017-6-8

@author: wuqi
'''
from flask import Flask,request
from bs4 import BeautifulSoup
from FlaskDemo.Demo import wechatText, wechatEnvent

# import DBConnect
# from FlaskDemo.DBConnect import dbModify
# appid='wx3418d0ea923e2cab'
# appsecret='a6484ab5228fe16548078852a442838f'
# from flask_wechat import filters, WeChat
app = Flask(__name__)
# @app.route('/weichat/')
# http://10.120.21.227:5001/weichat/?username=wqefds
# def validate():
#     username=request.args.get('username')
#     print username
#     return 'hello %s',username

@app.route('/wechat/',methods=['GET','POST'])   
def WeChatServer():
    print request.method
    if request.method =='GET': 
        echostr=request.args.get('echostr')  #encript signature  
#         timestamp=request.args.get('timestamp')  #time stamp    
#         nonce=request.args.get('nonce')
        print 'echostr is: ',echostr         #random    
        #Token     
        return echostr 
        #sha1 encript  
        #hashcode == signature,return True
    elif request.method =='POST':
        print "POST REQUEST"
        webcontent = request.get_data()
        soup = BeautifulSoup(webcontent,"html.parser")
        print soup
        
        msg_type = soup.msgtype.get_text()#get Evnet Type : text ,click,image
        
        if msg_type =='text':
            print 'MSG Type is Text'
            # <xml><tousername><![CDATA[gh_a14f1a9409ff]]></tousername>
            # <fromusername><![CDATA[oF8Buwo8-nOOERm9Lman4u7tCIAU]]></fromusername>
            # <createtime>1496998837</createtime>
            # <msgtype><![CDATA[text]]></msgtype>
            # <content><![CDATA[helloworld]]></content>
            # <msgid>6429561047487714993</msgid>
            # </xml>
            MSG = soup.content.get_text()
               
            print MSG
            # str="<xml>"
            # str+="<ToUserName><![CDATA[oF8Buwo8-nOOERm9Lman4u7tCIAU]]></ToUserName>"
            # str+="<FromUserName><![CDATA[gh_a14f1a9409ff]]></FromUserName>"
            # str+="<CreateTime>12345678</CreateTime>"
            # str+="<MsgType><![CDATA[text]]></MsgType>"
            # str+="<Content><![CDATA[hello"+MSG+"]]></Content>"
            # str+="</xml>"
             
            str= wechatText.Text(soup)
            return str
        if msg_type =='event':
            print 'MSG Type is event'
            event=soup.event.get_text()
            # <xml>
            # <ToUserName><![CDATA[toUser]]></ToUserName>
            # <FromUserName><![CDATA[FromUser]]></FromUserName>
            # <CreateTime>123456789</CreateTime>
            # <MsgType><![CDATA[event]]></MsgType>
            # <Event><![CDATA[subscribe]]></Event>
            # </xml>
            
            #insert Envent log to WX_USR_EVENT
            wechatEnvent.event(soup)
            print event
            if event =='subscribe':
#               ToUserName =soup.ToUserName.get_text()
                fromusername = soup.fromusername.get_text()
#               CreateTime = soup.CreateTime.get_text()
                print fromusername
                #insert User info to WX_USR_INFO
                nickname = wechatEnvent.subscribe(fromusername)
                print 'nickname:',nickname
                str="<xml>"
                str+="<ToUserName><![CDATA["+fromusername+"]]></ToUserName>"
                str+="<FromUserName><![CDATA[gh_a14f1a9409ff]]></FromUserName>"
                str+="<CreateTime>12345678</CreateTime>"
                str+="<MsgType><![CDATA[text]]></MsgType>"
                str+="<Content><![CDATA[hello "+nickname+"]]></Content>"
                str+="</xml>"
                return str
            if event =='unsubscribe':
                fromusername = soup.fromusername.get_text()
                print 'user unsubscribe !'
                
        else:
            print 'Unknow Msgtype:' ,msg_type      
      
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5001')
#     app.run(debug=True)






