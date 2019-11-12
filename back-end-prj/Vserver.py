'''
Created on 2019-11-12
suuport v covert from web request
flask based 
@author: wuqi2
'''

from flask import Flask,request
import pyhdb
from ffmpy import FFmpeg
import json
from flask_cors import CORS
from bokeh.core.properties import String
from celery.utils.serialization import jsonify

global false, null, true
false = null = true = ""

app = Flask(__name__)
CORS(app)

'''
{
"a":"astr",
"b":"bstr"
}
'''

@app.route('/vcv',methods=['POST'])   
def vconvert():
    data = request.get_data()
#     print (data)
    dictobj=json.loads(data)
    print(dictobj['a'])
    
#     ff =FFmpeg(
#     inputs={path: None},
#     outputs={'tester.m3u8': '-c:v libx264 -c:a aac -strict -2 -f hls -hls_list_size 0 -hls_time 2'}
#     )
#     print(ff.cmd)
#     ff.run()
    return data

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
    app.run(host='0.0.0.0',port='2222')
#     app.run(debug=True)
    