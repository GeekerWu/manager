'''
Created on 2019-11-12
suuport v covert from web request
flask based
@author: wuqi2
'''

import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685(0x40)
pwm2 = Adafruit_PCA9685.PCA9685(0x41)
pwm3 = Adafruit_PCA9685.PCA9685(0x42)


def set_servo_angle(channel, date):
    # date=4096*((angle*11)+500)/20000
    # date=int(4096*((angle*11)+500)/(20000)+0.5)
    date = date * 10
    print(channel, date)

    if channel <= 15:
        time.sleep(1)
        pwm.set_pwm(channel, 0, date)

    elif channel > 15 and channel <= 31:
        channel = channel - 16
        time.sleep(1)
        pwm2.set_pwm(channel, 0, date)

    elif channel > 31 and channel <= 48:
        channel = channel - 32
        time.sleep(1)
        pwm3.set_pwm(channel, 0, date)




import pymysql
from flask import Flask, request
from flask_socketio import SocketIO, emit


# import pyhdb
# from ffmpy import FFmpeg
import sqlite3
import json
from flask_cors import CORS

# from bokeh.core.properties import String
# from celery.utils.serialization import jsonify

global false, null, true
false = null = true = ""
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)
@app.route('/api/delete_init', methods=['POST'])
def deleteinit():
    deletechannel = request.get_data()
    # dictobj = json.loads(data)
    deletechannel =int(deletechannel)
    print('deletechannel:', deletechannel)
    # delete data:
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        port = 3306,
        db = 'ml',
        charset = 'utf8'
    )
    # 获取一个光标
    cursor = conn.cursor()
    # 定义将要执行的SQL语句
    sql = "delete from pose_init where channel=%s;"
    channel = deletechannel
    # 拼接并执行SQL语句
    cursor.execute(sql, [channel])
    # 涉及写操作注意要提交
    conn.commit()
    # 关闭连接
    cursor.close()
    conn.close()
    return 'done'


@app.route('/api/load_init', methods=['GET'])
def loadinit():
    #get data:
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        port = 3306,
        db = 'ml',
        charset = 'utf8'
    )
    # 获取一个光标
    cursor = conn.cursor()
    # 定义将要执行的SQL语句
    sql = "select * from pose_init;"
    # 拼接并执行SQL语句
    cursor.execute(sql)
    res = cursor.fetchall()  # 获取结果
    print('res', res)
    data ='';
    for item in res:
        #print('item:', item)
        if data=='':
            data = data + '[' + json.dumps(
                {"channel": item[0], "min": item[1], "max": item[2], "currval": item[3], "channel_name": item[4]})
        else:
            data=data+','+json.dumps({"channel":item[0],"min":item[1],"max":item[2], "currval":item[3], "channel_name":item[4]})
        #print('json item:',jsonitem)
    data=data+']'
    # print(dictobj['a'])
    # 关闭连接
    cursor.close()
    conn.close()
    print('data', data)
    resdata='{\"res\":'+data+'}'
    print('resdata',resdata)
    return resdata

@app.route('/api/save_init', methods=['POST'])
def saveinit():
    data = request.get_data()
    dictobj = json.loads(data)
    print ('res data:',dictobj)
    data=[];
    for item in dictobj:
        print('item:',item)
        # print('item:', item['channel'])
        data.append((item['channel'] ,item['min'],item['max'],item['currval'],item['channel_name']))
        # data.append('('+item['channel']+','+item['min']+','+item['max']+','+item['init']+')')
    # dictobj = json.loads(data)
    # print(dictobj['a'])
    print('sql data:',data)
    #insert data:
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        port = 3306,
        db = 'ml',
        charset = 'utf8'
    )
    # 获取一个光标
    cursor = conn.cursor()
    # 定义将要执行的SQL语句
    sql = "delete from pose_init;"
    # 拼接并执行SQL语句
    cursor.execute(sql)
    conn.commit()

    # 定义要执行的sql语句
    sql = "insert into pose_init(channel,min,max,init,channel_name) values(%s,%s,%s,%s,%s);"
    # data = [
    #     ('july', '147'),
    #     ('june', '258'),
    #     ('marin', '369')
    # ]
    # 拼接并执行sql语句
    cursor.executemany(sql, data)
    # 涉及写操作要注意提交
    conn.commit()
    # 关闭连接
    cursor.close()
    conn.close()

    return 'hahahha'

'''
{
"a":"astr",
"b":"bstr"
}
'''

@app.route('/vcv', methods=['POST'])
def vconvert():
    data = request.get_data()
    #     print (data)
    dictobj = json.loads(data)
    print(dictobj['a'])
    #     ff =FFmpeg(
    #     inputs={path: None},
    #     outputs={'tester.m3u8': '-c:v libx264 -c:a aac -strict -2 -f hls -hls_list_size 0 -hls_time 2'}
    #     )
    #     print(ff.cmd)
    #     ff.run()
    return data

@app.route('/getsql', methods=['GET'])
def getdata():
    coon = pymysql.connect(
    #host='localhost', user='test', passwd='test',
    host = 'localhost', user = 'root', passwd = 'root',
    port = 3306, db = 'mysql', charset = 'utf8'
    # port必须写int类型
    # charset必须写utf8，不能写utf-8
    )
    cur = coon.cursor()  # 建立游标
    cur.execute("select * from usr_info")  # 查询数据
    res = cur.fetchall()  # 获取结果
    resstr=''
    for item in res:
        print(item)
        resstr= resstr+item[0]
    cur.close()  # 关闭游标
    coon.close()  # 关闭连接

    # conn = sqlite3.connect('D:/manager/back-end-prj/test.db')
    # create_table_sql = '''
    # CREATE TABLE `user_info` (
    #                           `id` int(11) NOT NULL,
    #                           `name` varchar(20) NOT NULL,
    #                           `gender` varchar(4) DEFAULT NULL,
    #                           `age` int(11) DEFAULT NULL,
    #                           `address` varchar(200) DEFAULT NULL,
    #                           `phone` varchar(20) DEFAULT NULL,
    #                           `token` varchar(40) DEFAULT '4291d7da9005377ec9aec4a71ea837f',
    #                            PRIMARY KEY (`id`)
    #                         )
    # '''
    # cu = conn.cursor()
    # conn.execute(create_table_sql)
    # print('table create successful')
    # try:
    #
    # except sqlite3.Error as why:
    #     print( 'create table failed:' + why.args[0])
    return resstr
    #
    # fetchall_sql = '''SELECT * FROM student'''
    # try:
    #     conn = sqlite3.connect('test.db')
    #     cu = conn.cursor()
    #     cu.execute(fetchall_sql)
    #     content = cu.fetchall()
    #     print(content)
    #     # if len(content) > 0:
    #     #     for item in content:
    #     #         for element in item:
    #     #             print element,
    #     #         print ''
    #     # else:
    #     #     for element in content:
    #     #         print element,
    #     #     print ''
    #     return content
    # except sqlite3.Error as why:
    #     print ( "fetchall data failed:", why.args[0])
    #     return "fetchall data failed:", why.args[0]

@app.route('/web', methods=['GET', 'POST'])
def webServer():
    print(request.method)
    if request.method == 'GET':
        print("GET Header info:")
        print(str(request.headers))
        print("GET Body")
        data = request.get_data()
        print(data)
        print("Post Values")
        print(request.values)
        print("Post Form")
        print(request.form)
        print("GET REQUEST")
        resp = 'Get helloworld'
        #         resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    elif request.method == 'POST':
        print("Header info:")
        print(str(request.headers))
        print("POST Body")
        data = request.get_data()
        print(data)
        print("Post Values")
        print(request.values)
        print("Post Form")
        print(request.form)
        #       print request.values
        Result = data
        # Result = json.loads(data)
        print(Result)
        #         setHeader("Access-Control-Allow-Origin", "*")
        # resp=json.dumps(Result)
        resp = Result
        return resp
        print(resp)
        return resp
    else:
        print("Else")
        resp = 'Post helloworld'
        return resp

@app.route('/api/auth/login', methods=['POST'])
def vueServer():
    if request.method == 'POST':
        print("Header info:")
        print(str(request.headers))
        print("POST Body")
        data = request.get_data()
        print(data)
        print("Post Values")
        print(request.values)
        print("Post Form")
        print(request.form)
        #       print request.values
        Result = json.loads(data)
        # Result = json.loads(data)
        print(Result)
        #         setHeader("Access-Control-Allow-Origin", "*")
        res = {
            "result": {
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
        resp = json.dumps(res)
        #         resp=Result
        # return resp
        #         print(resp)
        return resp

@app.route('/api/auth/2step-code', methods=['POST'])
def twostep_code():
    if request.method == 'POST':
        print("Header info:")
        print(str(request.headers))
        print("POST Body")
        data = request.get_data()
        print(data)
        #         print ("get Values")
        print(request.values)
        print("Post Form")
        print(request.form)
        #
        res = {"stepCode": 1}
    resp = json.dumps(res)
    #         resp=jsonify(res)
    #         resp=Result
    # return resp
    #     print(resp)
    return resp


@app.route('/api/auth/logout', methods=['POST'])
def logout():
    res = {"stepCode": 1}
    resp = json.dumps(res)
    return resp

@app.route('/api/user/info', methods=['GET'])
def vuerouter():
    if request.method == 'GET':
        print("Header info:")
        print(str(request.headers))
        #         print ("POST Body")
        #         data = request.get_data()
        #         print (data)
        print("get Values")
        print(request.values)
        #         print ("Post Form")
        #         print (request.form)
        #       print request.values
        #         Result =json.loads(data)
        # Result = json.loads(data)
        #         print (Result)
        #         setHeader("Access-Control-Allow-Origin", "*")
        res = {
            "result": {
                "id": "4291d7da9005377ec9aec4a71ea837f",
                "name": "哈哈哈",
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

        resp = json.dumps(res)
        #         resp=jsonify(res)
        #         resp=Result
        # return resp
        #     print(resp)
        return resp

# if __name__ == "__main__":
#     app.run(host='0.0.0.0',port='2222')
# #     app.run(debug=True)

"""
对socketio进行一些监听设置
"""

@socketio.on('subscribe', namespace='/test')
def subscribe(data):
    print('request_for_client calling from client', data)
    #     socketio.
    #     if task ='':
    #     global thread
    # if thread is None:
    #         print('Task is not run init a new task')
    #         thread=socketio.start_background_task(schedule_check)
    #         print(thread)
    #     else:
    # print('thread already run')
    print('done')

@socketio.on('message', namespace='/test')
def message(data):
    print('recived message', data)
    # print(type(data))
    # json.dumps(data)
    # data = json.loads(data)

    print(data['msg'])
    if (data['username'] == 'pose'):
        channel = 22
        set_servo_angle(channel, data['msg'])

    #     socketio.
    #     if task ='':
    #     global thread
    # if thread is None:
    #         print('Task is not run init a new task')
    #         thread=socketio.start_background_task(schedule_check)
    #         print(thread)
    #     else:
    # print('thread already run')
    print('done')
    emit('response', {'code': '200', 'msg': data['msg']}, namespace='/test')
    print(data['msg'])

    # coon = pymysql.connect(
    #     # host='localhost', user='test', passwd='test',
    #     host='localhost', user='root', passwd='root',
    #     port=3306, db='ml', charset='utf8'
    #     # port必须写int类型
    #     # charset必须写utf8，不能写utf-8
    # )
    # cur = coon.cursor()  # 建立游标
    # cur.execute("select * from usr_info")  # 查询数据
    # res = cur.fetchall()  # 获取结果
    # resstr = ''
    # itemstr=""
    # i=0
    # for item in res:
    #     print(item)
    #     itemstr="".join([str(x)for x in item])
    #     resstr = resstr+str(i)+':'+ str(itemstr)+','
    #     i=i+1
    # cur.close()  # 关闭游标
    # coon.close()  # 关闭连接
    #
    # #     socketio.
    # #     if task ='':
    # #     global thread
    # # if thread is None:
    # #         print('Task is not run init a new task')
    # #         thread=socketio.start_background_task(schedule_check)
    # #         print(thread)
    # #     else:
    # # print('thread already run')
    # print(resstr)
    # print('done')
    # emit('response', {'code': '200', 'msg': data['msg']}, namespace='/test')

@socketio.on('connect')
def connect():
    print('connect ')
    print('sent response')
    emit('connected', {'code': '200', 'msg': 'connected'}, namespace='/test')

#     task=socketio.start_background_task(schedule_check())
#     time.sleep(5)
#     emit('message',{'code':'200','msg':'hahahha'})
#     print('sid ',sid)
#     print('environ ',environ)

@socketio.on('disconnect', namespace='/test')
def disconnect():
    print('disconnect ')
    emit('disconnect', {'code': '200', 'msg': 'disconnect'})

#     print('sid ',sid)
#     print('environ ',environ)

if __name__ == '__main__':
    socketio.run(app, debug=false, host='0.0.0.0', port=2222)