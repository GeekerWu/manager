'''
Created on 2018-6-7

@author: wuqi2
'''

# from flask import Flask,request
#support download
from flask import Flask,request,render_template,send_file, send_from_directory,json,jsonify,make_response
import pyhdb
import json
import os
from flask_cors import CORS
from bokeh.core.properties import String
from celery.utils.serialization import jsonify
import datetime
import time
from docutils.writers.odf_odt import ToString
from nltk.corpus.reader.pl196x import SENT
global false, null, true
false = null = true = ""

app = Flask(__name__)
download_folder = 'D:/workspace/Flask/FlaskDemo/download'
app.config['download_folder'] = download_folder
CORS(app)
@app.route('/dl/<path:filename>',methods=['GET'])   
def dl(filename):
    directory = app.config['download_folder']
    print (request.method)
    try:
        response = make_response(
            send_from_directory(directory,filename, as_attachment=True))
        return response
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)})





    
@app.route('/getdata',methods=['GET'])   
def getdata():
    print (request.method)
    items=''
    loop=0
    item ='''
    {
        "athlete": "Michael Phelps",
        "age": 23,
        "country": "United States",
        "year": 2008,
        "date": "24/08/2008",
        "sport": "Swimming",
        "gold": 8,
        "silver": 0,
        "bronze": 0,
        "total": 8,
        "col11": 1,
        "col12": 1,
        "col13": 1,
        "col14": 1,
        "col15": 1,
        "col16": 1,
        "col17": 1,
        "col18": 1,
        "col19": 1,
        "col20": 1,
        "col21": 1,    
     '''
    while loop<1:
        items=items+item+ '''"grp":'''+str(loop)+'''},'''
        loop=loop+1
        print(loop)
    else:
        res='''['''+items
        res=res+''' {
                "athlete": "Michael Phelps",
                "age": 23,
                "country": "United States",
                "year": 2008,
                "date": "24/08/2008",
                "sport": "Swimming",
                "gold": 8,
                "silver": 0,
                "bronze": 0,
                "total": 8,
                "col11": 1,
                "col12": 1,
                "col13": 1,
                "col14": 1,
                "col15": 1,
                "col16": 1,
                "col17": 1,
                "col18": 1,
                "col19": 1,
                "col20": 1,
                "col21": 1,           
                '''
        res=res+'''"grp":'''+str(loop+1)+'''}'''
        res=res+''' ]'''
        
        print('dataready')
        with open('test_data.json', 'w') as json_file:
            json_file.write(res)
            json_file.close()
        return jsonify(res)
#                 "col11": 1,
#                 "col12": 1,
#                 "col13": 1,
#                 "col14": 1,
#                 "col15": 1,
#                 "col16": 1,
#                 "col17": 1,
#                 "col18": 1,
#                 "col19": 1,
#                 "col20": 1,
#                 "col21": 1,
#                 "col22": 1,
#                 "col23": 1,
#                 "col24": 1,

@app.route('/dataset')
def hello():
    with open(os.path.join('D:/workspace/Flask/FlaskDemo', 'test_data.json')) as f:
         s=f.read()
         f.close()
    return jsonify(s)


@app.route('/web',methods=['GET','POST'])   
def webServer():
    print (request.method)
    if request.method =='GET':
        print ("GET Header info:")
        print (str(request.headers))
        print ("GET Body")
        data = request.get_data()
        print (data)
        print ("Post Values")
        print (request.values)
        print ("Post Form")
        print (request.form)
        print ("GET REQUEST") 
        resp = 'Get helloworld' 
#         resp.headers['Access-Control-Allow-Origin'] = '*'
        
        return resp
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
#       print request.values
        Result =data
        #Result = json.loads(data)
        print (Result)
#         setHeader("Access-Control-Allow-Origin", "*")
        #resp=json.dumps(Result)
        resp=Result
    
        return resp
        print(resp)
        
        return resp
    else :
        print ("Else")
        
        resp = 'Post helloworld' 
        
        
        return resp
@app.route('/polaris_api/login',methods=['POST'])
def vueServer():
    if request.method =='POST':
        print ("Header info:")
        print (str(request.headers))
        print ("POST Body")
        data = request.get_data()
        print (data)
        print ("Post Values")
        print (request.values)
        print ("Post Form")
        print (request.form)
#       print request.values
        Result =json.loads(data)
        #Result = json.loads(data)
        print (Result)
#         setHeader("Access-Control-Allow-Origin", "*")
        res={
             "result":{
                "id": "guid",
                "name": "name",
                "username": "admin",
                "password": "",
                "avatar": "https://gw.alipayobjects.com/zos/rmsportal/jZUIxmJycoymBprLOUbT.png",
                "status": 1,
                "telephone": "",
                "lastLoginIp": "27.154.74.117",
                "lastLoginTime": 1534837621348,
                "creatorId": "admin",
                "createTime": 1497160610259,
                "deleted": 0,
                "roleId": "admin",
                "lang": "zh-CN",
                "token": "4291d7da9005377ec9aec4a71ea837f"
          }
        }
        
        
#         res=json.loads(res)
        resp=json.dumps(res)
#         resp=Result
    
        #return resp
#         print(resp)
        
        return resp

@app.route('/polaris_api/2step-code',methods=['POST'])
def twostep_code():
    if request.method =='POST':
        print ("Header info:")
        print (str(request.headers))
        print ("POST Body")
        data = request.get_data()
        print (data)
#         print ("get Values")
        print (request.values)
        print ("Post Form")
        print (request.form)
#         
        res={ "stepCode": 1 }
    resp=json.dumps(res)
#         resp=jsonify(res)
#         resp=Result
    
        #return resp
#     print(resp)
        
    return resp
        
@app.route('/polaris_api/logout',methods=['POST'])
def logout(): 
    res={ "stepCode": 1 }
    resp=json.dumps(res)       
    return resp

@app.route('/polaris_api/userinfo',methods=['GET'])
def vuerouter():
     if request.method =='GET':
        print ("Header info:")
        print (str(request.headers))
#         print ("POST Body")
#         data = request.get_data()
#         print (data)
        print ("get Values")
        print (request.values)
#         print ("Post Form")
#         print (request.form)
#       print request.values
#         Result =json.loads(data)
        #Result = json.loads(data)
#         print (Result)
#         setHeader("Access-Control-Allow-Origin", "*")
        res={
             "result":{
                        "id": "4291d7da9005377ec9aec4a71ea837f",
                        "name": "天野远子",
                        "username": "admin",
                        "password": "",
                        "avatar": "/avatar2.jpg",
                        "status": 1,
                        "telephone": "",
                        "lastLoginIp": "27.154.74.117",
                        "lastLoginTime": 1534837621348,
                        "creatorId": "admin",
                        "createTime": 1497160610259,
                        "merchantCode": "TLif2btpzg079h15bk",
                        "deleted": 0,
                        "roleId": "admin",
                        "role": {
                            "id": "admin",
                            "name": "管理员",
                            "describe": "拥有所有权限",
                            "status": 1,
                            "creatorId": "system",
                            "createTime": 1497160610259,
                            "deleted": 0,
                            "permissions": [{
                                "roleId": "admin",
                                "permissionId": "support",
                                "permissionName": "超级模块",
                                "actions": "[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"import\",\"defaultCheck\":false,\"describe\":\"导入\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"},{\"action\":\"export\",\"defaultCheck\":false,\"describe\":\"导出\"}]",
                                "actionEntitySet": [{
                                    "action": "add",
                                    "describe": "新增",
                                    "defaultCheck": false
                                }, {
                                    "action": "import",
                                    "describe": "导入",
                                    "defaultCheck": false
                                }, {
                                    "action": "get",
                                    "describe": "详情",
                                    "defaultCheck": false
                                }, {
                                    "action": "update",
                                    "describe": "修改",
                                    "defaultCheck": false
                                }, {
                                    "action": "delete",
                                    "describe": "删除",
                                    "defaultCheck": false
                                }, {
                                    "action": "export",
                                    "describe": "导出",
                                    "defaultCheck": false
                                }],
                                "actionList": null,
                                "dataAccess": null
                            }, {
                                "roleId": "admin",
                                "permissionId": "dashboard",
                                "permissionName": "仪表盘",
                                "actions": "[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]",
                                "actionEntitySet": [{
                                    "action": "add",
                                    "describe": "新增",
                                    "defaultCheck": false
                                }, {
                                    "action": "query",
                                    "describe": "查询",
                                    "defaultCheck": false
                                }, {
                                    "action": "get",
                                    "describe": "详情",
                                    "defaultCheck": false
                                }, {
                                    "action": "update",
                                    "describe": "修改",
                                    "defaultCheck": false
                                }, {
                                    "action": "delete",
                                    "describe": "删除",
                                    "defaultCheck": false
                                }],
                                "actionList": null,
                                "dataAccess": null
                            }, {
                                "roleId": "admin",
                                "permissionId": "exception",
                                "permissionName": "异常页面权限",
                                "actions": "[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]",
                                "actionEntitySet": [{
                                    "action": "add",
                                    "describe": "新增",
                                    "defaultCheck": false
                                }, {
                                    "action": "query",
                                    "describe": "查询",
                                    "defaultCheck": false
                                }, {
                                    "action": "get",
                                    "describe": "详情",
                                    "defaultCheck": false
                                }, {
                                    "action": "update",
                                    "describe": "修改",
                                    "defaultCheck": false
                                }, {
                                    "action": "delete",
                                    "describe": "删除",
                                    "defaultCheck": false
                                }],
                                "actionList": null,
                                "dataAccess": null
                            }, {
                                "roleId": "admin",
                                "permissionId": "result",
                                "permissionName": "结果权限",
                                "actions": "[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]",
                                "actionEntitySet": [{
                                    "action": "add",
                                    "describe": "新增",
                                    "defaultCheck": false
                                }, {
                                    "action": "query",
                                    "describe": "查询",
                                    "defaultCheck": false
                                }, {
                                    "action": "get",
                                    "describe": "详情",
                                    "defaultCheck": false
                                }, {
                                    "action": "update",
                                    "describe": "修改",
                                    "defaultCheck": false
                                }, {
                                    "action": "delete",
                                    "describe": "删除",
                                    "defaultCheck": false
                                }],
                                "actionList": null,
                                "dataAccess": null
                            }, {
                                "roleId": "admin",
                                "permissionId": "profile",
                                "permissionName": "详细页权限",
                                "actions": "[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]",
                                "actionEntitySet": [{
                                    "action": "add",
                                    "describe": "新增",
                                    "defaultCheck": false
                                }, {
                                    "action": "query",
                                    "describe": "查询",
                                    "defaultCheck": false
                                }, {
                                    "action": "get",
                                    "describe": "详情",
                                    "defaultCheck": false
                                }, {
                                    "action": "update",
                                    "describe": "修改",
                                    "defaultCheck": false
                                }, {
                                    "action": "delete",
                                    "describe": "删除",
                                    "defaultCheck": false
                                }],
                                "actionList": null,
                                "dataAccess": null
                            }, {
                                "roleId": "admin",
                                "permissionId": "table",
                                "permissionName": "表格权限",
                                "actions": "[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"import\",\"defaultCheck\":false,\"describe\":\"导入\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"}]",
                                "actionEntitySet": [{
                                    "action": "add",
                                    "describe": "新增",
                                    "defaultCheck": false
                                }, {
                                    "action": "import",
                                    "describe": "导入",
                                    "defaultCheck": false
                                }, {
                                    "action": "get",
                                    "describe": "详情",
                                    "defaultCheck": false
                                }, {
                                    "action": "update",
                                    "describe": "修改",
                                    "defaultCheck": false
                                }],
                                "actionList": null,
                                "dataAccess": null
                            }, {
                                "roleId": "admin",
                                "permissionId": "form",
                                "permissionName": "表单权限",
                                "actions": "[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]",
                                "actionEntitySet": [{
                                    "action": "add",
                                    "describe": "新增",
                                    "defaultCheck": false
                                }, {
                                    "action": "get",
                                    "describe": "详情",
                                    "defaultCheck": false
                                }, {
                                    "action": "query",
                                    "describe": "查询",
                                    "defaultCheck": false
                                }, {
                                    "action": "update",
                                    "describe": "修改",
                                    "defaultCheck": false
                                }, {
                                    "action": "delete",
                                    "describe": "删除",
                                    "defaultCheck": false
                                }],
                                "actionList": null,
                                "dataAccess": null
                            }, {
                                "roleId": "admin",
                                "permissionId": "order",
                                "permissionName": "订单管理",
                                "actions": "[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]",
                                "actionEntitySet": [{
                                    "action": "add",
                                    "describe": "新增",
                                    "defaultCheck": false
                                }, {
                                    "action": "query",
                                    "describe": "查询",
                                    "defaultCheck": false
                                }, {
                                    "action": "get",
                                    "describe": "详情",
                                    "defaultCheck": false
                                }, {
                                    "action": "update",
                                    "describe": "修改",
                                    "defaultCheck": false
                                }, {
                                    "action": "delete",
                                    "describe": "删除",
                                    "defaultCheck": false
                                }],
                                "actionList": null,
                                "dataAccess": null
                            }, {
                                "roleId": "admin",
                                "permissionId": "permission",
                                "permissionName": "权限管理",
                                "actions": "[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]",
                                "actionEntitySet": [{
                                    "action": "add",
                                    "describe": "新增",
                                    "defaultCheck": false
                                }, {
                                    "action": "get",
                                    "describe": "详情",
                                    "defaultCheck": false
                                }, {
                                    "action": "update",
                                    "describe": "修改",
                                    "defaultCheck": false
                                }, {
                                    "action": "delete",
                                    "describe": "删除",
                                    "defaultCheck": false
                                }],
                                "actionList": null,
                                "dataAccess": null
                            }, {
                                "roleId": "admin",
                                "permissionId": "role",
                                "permissionName": "角色管理",
                                "actions": "[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]",
                                "actionEntitySet": [{
                                    "action": "add",
                                    "describe": "新增",
                                    "defaultCheck": false
                                }, {
                                    "action": "get",
                                    "describe": "详情",
                                    "defaultCheck": false
                                }, {
                                    "action": "update",
                                    "describe": "修改",
                                    "defaultCheck": false
                                }, {
                                    "action": "delete",
                                    "describe": "删除",
                                    "defaultCheck": false
                                }],
                                "actionList": null,
                                "dataAccess": null
                            }, {
                                "roleId": "admin",
                                "permissionId": "table",
                                "permissionName": "桌子管理",
                                "actions": "[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"query\",\"defaultCheck\":false,\"describe\":\"查询\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"}]",
                                "actionEntitySet": [{
                                    "action": "add",
                                    "describe": "新增",
                                    "defaultCheck": false
                                }, {
                                    "action": "get",
                                    "describe": "详情",
                                    "defaultCheck": false
                                }, {
                                    "action": "query",
                                    "describe": "查询",
                                    "defaultCheck": false
                                }, {
                                    "action": "update",
                                    "describe": "修改",
                                    "defaultCheck": false
                                }, {
                                    "action": "delete",
                                    "describe": "删除",
                                    "defaultCheck": false
                                }],
                                "actionList": null,
                                "dataAccess": null
                            }, {
                                "roleId": "admin",
                                "permissionId": "user",
                                "permissionName": "用户管理",
                                "actions": "[{\"action\":\"add\",\"defaultCheck\":false,\"describe\":\"新增\"},{\"action\":\"import\",\"defaultCheck\":false,\"describe\":\"导入\"},{\"action\":\"get\",\"defaultCheck\":false,\"describe\":\"详情\"},{\"action\":\"update\",\"defaultCheck\":false,\"describe\":\"修改\"},{\"action\":\"delete\",\"defaultCheck\":false,\"describe\":\"删除\"},{\"action\":\"export\",\"defaultCheck\":false,\"describe\":\"导出\"}]",
                                "actionEntitySet": [{
                                    "action": "add",
                                    "describe": "新增",
                                    "defaultCheck": false
                                }, {
                                    "action": "import",
                                    "describe": "导入",
                                    "defaultCheck": false
                                }, {
                                    "action": "get",
                                    "describe": "详情",
                                    "defaultCheck": false
                                }, {
                                    "action": "update",
                                    "describe": "修改",
                                    "defaultCheck": false
                                }, {
                                    "action": "delete",
                                    "describe": "删除",
                                    "defaultCheck": false
                                }, {
                                    "action": "export",
                                    "describe": "导出",
                                    "defaultCheck": false
                                }],
                                "actionList": null,
                                "dataAccess": null
                            }]
                        }
                    }
             }
        
        resp=json.dumps(res)
#         resp=jsonify(res)
#         resp=Result
    
        #return resp
#     print(resp)
        
        return resp
        
        
    
 
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8088)
#     app.run(debug=True)
    