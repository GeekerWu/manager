'''
Created on 2017-6-16

@author: wuqi2
'''
import pyhdb
#import json
import json
from time import sleep

# connection =pyhdb.connect(
#     host="10.99.202.74",
#     port=30015,
#     user="WUQI2",
#     password='Initial0'
# )

connection =pyhdb.connect(
    host="10.122.13.22",
    port=30353,
    user="SCI_APPLICATION",
    password='Initial0'
)

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