'''
Created on 2018-11-22

@author: wuqi2
'''
from time import sleep
from flask import Flask,request
import pyRserve
import pyhdb
import json
from flask_cors import CORS
from bokeh.core.properties import String

connection =pyhdb.connect(
    host="10.122.13.22",
    port=30353,
    user="SCI_APPLICATION",
    password='Initial0'
)

app = Flask(__name__)
CORS(app)
@app.route('/Rserve',methods=['POST'])   
def webServer():
    print (request.method)
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
#         print request.values
        Result =data
        #Result = json.loads(data)
        print (Result)
#         setHeader("Access-Control-Allow-Origin", "*")
#         #resp=json.dumps(Result)
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM SCI.WORD_CLOUD")
#         res = cursor.fetchmany(2)
#         
#         #res convert to Json
#         column =['KEY_WORD','FREQ']
#         row_index=0
#         JsonStr="";
#         for row in res:
#             column_index = 0
#             row_data =""
#             for data in row:
#         #         print (column_index)
#         #         print (len(column))
#                 if column_index ==0:
#                     column_data = "{\""+column[column_index]+"\":\""+str(data)+"\"," 
#                 elif column_index < len(column)-1:
#                     column_data = "\""+column[column_index]+"\":\""+str(data)+"\","
#                 else:
#                     column_data = "\""+column[column_index]+"\":\""+str(data)+"\"}"
#                 column_index=column_index+1     
#         #         print (row_data)
#                 row_data=row_data+column_data
#         #     print ("Row"+row_data)   
#             if row_index==0:
#                 JsonStr = "{ \"data\":["+row_data+","
#             elif row_index <len(res)-1:
#                 JsonStr = JsonStr+row_data+","
#             else:
#                 JsonStr =JsonStr+row_data+"]}"
#             row_index=row_index+1
#             
#         # print ("JsonStr"+JsonStr)
#         Result = json.loads(JsonStr)
#         print (Result)
#                 
#         # res_json=json.dump(res)
#         # print ('Jsong Fomart is:',res_json)
#         print ("res is:",res)
#         print ("row1 is:",res[0])
#         print ("column1 is",res[0][0])
#         sleep(10)
#         connection.close()
#         print ("connection close")
        
        resp=Result
        return resp
        print(resp)
        return resp
    else :
        print ("other request method")
        resp = 'other request method' 
        return resp


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
        #resp = 'Get helloworld' 
        #resp.headers['Access-Control-Allow-Origin'] = '*'
        
        conn = pyRserve.connect(host='10.120.21.227',port=6666)
        #print(str(conn.isClosed()))
        #Defect_Analysis_Loading_Data.R
        #Defect_Analysis_Word_Frequence.R
        resp = conn.eval('source("C:/Users/Administrator/Desktop/RScript/DefectAnalysis/txtAnalysisFreq.R")')
        conn.close()
        print('done')
        return 'hahah'
        #return 'get method hello world'
    
    
    #post to get Hana connection
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
        Result =data
        #Result = json.loads(data)
        print (Result)
#         setHeader("Access-Control-Allow-Origin", "*")
        #resp=json.dumps(Result)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM SCI.WORD_CLOUD")
        res = cursor.fetchmany(2)
        
        #res convert to Json
        column =['KEY_WORD','FREQ']
        row_index=0
        JsonStr="";
        for row in res:
            column_index = 0
            row_data =""
            for data in row:
        #         print (column_index)
        #         print (len(column))
                if column_index ==0:
                    column_data = "{\""+column[column_index]+"\":\""+str(data)+"\"," 
                elif column_index < len(column)-1:
                    column_data = "\""+column[column_index]+"\":\""+str(data)+"\","
                else:
                    column_data = "\""+column[column_index]+"\":\""+str(data)+"\"}"
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
                
        # res_json=json.dump(res)
        # print ('Jsong Fomart is:',res_json)
        print ("res is:",res)
        print ("row1 is:",res[0])
        print ("column1 is",res[0][0])
        sleep(10)
        connection.close()
        print ("connection close")
        
        resp=Result
        return resp
        print(resp)
        return resp
    else :
        print ("Else")
        resp = 'Post helloworld' 
        
        return resp
           
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='666')
#     app.run(debug=True)

# connection =pyhdb.connect(
#     host="10.99.202.74",
#     port=30015,
#     user="WUQI2",
#     password='Initial0'
# )





