'''
Created on 2016-1-12

@author: wuqi2
'''

import cx_Oracle  

# conn=cx_Oracle.connect('MOBILEABPP/MOBILEABPP@TSTMDMN') 
conn=cx_Oracle.connect('PCGSDC/PCGSDC@TSTCSEN') 

c=conn.cursor()

# x=c.execute('SELECT tel FROM USR_PROFILE WHERE LOGIN_NAME=\'admin\'')
sqlstr='''
select to_char(scn_to_timestamp(max(ora_rowscn)),'yyyy-mm-dd hh24:mi:ss') as lats_dml_time from Z_UI_RESEND_REQUEST
'''


x=c.execute(sqlstr)


print (x.fetchone()[0])


c.close()

conn.close() 