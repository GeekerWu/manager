'''
Created on 2018-12-3

@author: wuqi2
'''
import pyRserve
from pyRserve.rtypes import RESP_OK
conn = pyRserve.connect(host='10.120.21.227',port=6666)
#conn = pyRserve.connect(host='localhost',port=6666)
#print(str(conn.isClosed()))
#Defect_Analysis_Loading_Data.R
#Defect_Analysis_Word_Frequence.R
resp = conn.eval('source("C:/Users/Administrator/Desktop/RScript/DefectAnalysis/Defect_Analysis_Loading_Data.R")')

resp = conn.eval('source("C:/Users/Administrator/Desktop/RScript/DefectAnalysis/Defect_Analysis_Word_Frequence.R")')
conn.close()
print('done')