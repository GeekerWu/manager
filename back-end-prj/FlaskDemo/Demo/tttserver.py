'''
Created on 2018-6-7

@author: wuqi2
'''

# from flask import Flask,request
#support download
from flask import Flask,request
# ,render_template,send_file, send_from_directory,json,jsonify,make_response
# import pyhdb
# import json
import os
from flask_cors import CORS
# from bokeh.core.properties import String
# from celery.utils.serialization import jsonify
# import datetime
# import time
# from docutils.writers.odf_odt import ToString
# from nltk.corpus.reader.pl196x import SENT
# global false, null, true
# false = null = true = ""

app = Flask(__name__)

CORS(app)



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

        

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8088)
#     app.run(debug=True)
    