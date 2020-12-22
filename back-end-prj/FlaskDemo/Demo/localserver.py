'''
Created on 2020-8-5

@author: wuqi2
'''

# from flask import Flask,request
#support download
from flask import Flask,request,render_template,send_file, send_from_directory,json,jsonify,make_response
import json
import os
from flask_cors import CORS
from celery.utils.serialization import jsonify
false = null = true = ""

app = Flask(__name__)
CORS(app)
@app.route('/columndef',methods=['GET'])   
def columndef():
    print (request.method)
    res='''
   [{
        "headerName": "A",
        "field": "a",
        "dataType": "string",
        "enableRowGroup": "left",
        "enablePivot": "300"
    },{
        "headerName": "B",
        "field": "b",
        "dataType": "string",
        "enableRowGroup": "left",
        "enablePivot": "100"
    }]
   '''
    print('return column defs')
    return jsonify(res)

@app.route('/rowdata',methods=['GET'])   
def rowdata():
    print (request.method)
    res='''[
           {"a":"aaaa","b":"bbbb"},
           {"a":"aaa","b":"bbb"},
           {"a":"aa","b":"bb"}
           ]
   '''
    print(' return rowdata')
    return jsonify(res)


@app.route('/filterList',methods=['GET'])   
def filterlist():
    print (request.method)
    res='''
    [
    {
    "index": "0",
    "label": "Type",
    "decorator": "type",
    "required": "false",
    "allowClear": true,
    "editDisabled": false,
    "message": "Please select",
    "placeHolder": "Please select",
    "inputType": "dropDown",
    "text": "",
    "dropDownList": ["ItemNo","B/S"]
    },
    {
        "index": "1",
        "label": "Item Owner",
        "decorator": "Owner",
        "required": false,
        "allowClear": true,
        "editDisabled": false,
        "message": "Please select",
        "placeHolder": "Please select",
        "inputType": "input",
        "text": "''",
        "dropDownList": "[]"
    }
           ]
   '''
    print(' return filterList')
    return jsonify(res)
   
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8088)
#     app.run(debug=True)
    