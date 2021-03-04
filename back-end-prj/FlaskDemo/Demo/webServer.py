'''
Created on 2017-6-13
@author: wuqi
'''
from flask import Flask,request
import pyhdb
import json
from bokeh.core.properties import String
# from time import sleep
# from bs4 import BeautifulSoup
# from FlaskDemo import wechatEnvent
# from FlaskDemo import wechatText
# import urllib
# import json
# import AccToken
# import DBConnect
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
@app.route('/web',methods=['GET','OPTIONS','POST'])   
def webServer():
    print (request.method)
    if request.method =='GET':
        print ("GET REQUEST") 
        return 'helloworld' 
    elif request.method =='POST':
        print ("Header info:")
        print (str(request.headers))
        print ("POST Body")
        data = request.get_data()
        print (data)
        print ("Post Values")
        print (request.values)
        print ("Post Form")
        print (request.form)
#         print request.values
        return 'helloworld' +str(data)
    else :
        print ("Else")
        return "hello"
@app.route('/webhana')
def hanna():
    data = request.get_data()
    print (data)
#     if request.method =='GET':
    if True:
        print ("GET REQUEST") 
        connection =pyhdb.connect(
            host="10.99.202.74",
            port=30015,
            user="WUQI2",
            password='Initial0'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT MTM,GEO,DN_NUM FROM SCI.Z_MBG_ORD_KPI")
        res = cursor.fetchmany(4)
#         assert(1==2)
        #res convert to Json
        column =['MTM','GEO','DN_NUM']
        row_index=0
        JsonStr="";
        for row in res:
            column_index = 0
            row_data =""
            for data in row:
        #         print (column_index)
        #         print (len(column))
                if column_index ==0:
                    column_data = "{\""+column[column_index]+"\":\""+data+"\"," 
                elif column_index < len(column)-1:
                    column_data = "\""+column[column_index]+"\":\""+data+"\","
                else:
                    column_data = "\""+column[column_index]+"\":\""+data+"\"}"
                column_index=column_index+1     
        #         print (row_data)
                row_data=row_data+column_data
        #     print ("Row"+row_data)   
            if row_index==0:
                JsonStr = "{ \"data\":["+row_data+","
            elif row_index <len(res)-1:
                JsonStr = JsonStr+row_data+","
            else:
                JsonStr =JsonStr+row_data+"]}"
            row_index=row_index+1
        # print ("JsonStr"+JsonStr)
        Result = json.loads(JsonStr)
        print (Result)
#         setHeader("Access-Control-Allow-Origin", "*")
        resp=json.dumps(Result)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
#         return 'helloworld' 
#     if request.method =='POST':
#         print ("GET REQUEST") 
#         return 'helloworld' 
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5001')
#     app.run(debug=True)






