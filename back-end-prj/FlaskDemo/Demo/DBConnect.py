'''
Created on 2017-6-9

@author: wuqi
'''
import cx_Oracle

def dbModify(SQLstr):
    conn=cx_Oracle.connect('MOBILEABPP/MOBILEABPP@TSTMDM') 
    c=conn.cursor()
    #x=c.execute("Insert into MOBILEABPP.PRODUCT_INFO(ID, NAME, PRICE, RANK, ONSALE_DATE, NETWORK_TYPE, FOURG_NET, MAINSCREENSIZE, CPU_TYPE, CPU_NAME, BATTERY, CAMERA, OS)Values('1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1')")
    SQLstr = SQLstr.replace(u'\xae',u' ')
    SQLstr =SQLstr.replace(u'\u2122',u' ')
    resp=c.execute(SQLstr.replace(u'\xa0',u' '))
    x=c.execute("commit")
    #INSTER INTO PRODUCT_INFO
    #print x.fetchall()[2][1]
    c.close()
    conn.close() 
    return  resp

def dbSelect(SQLstr):
    conn=cx_Oracle.connect('MOBILEABPP/MOBILEABPP@TSTMDM') 
    c=conn.cursor()
    #x=c.execute("Insert into MOBILEABPP.PRODUCT_INFO(ID, NAME, PRICE, RANK, ONSALE_DATE, NETWORK_TYPE, FOURG_NET, MAINSCREENSIZE, CPU_TYPE, CPU_NAME, BATTERY, CAMERA, OS)Values('1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1')")
    SQLstr =SQLstr.replace(u'\xae',u' ')
    SQLstr =SQLstr.replace(u'\u2122',u' ')
    result=c.execute(SQLstr.replace(u'\xa0',u' '))
    #INSTER INTO PRODUCT_INFO
    #print x.fetchall()[2][1]
    return result
    c.close()
    conn.close() 
    
def updateAccToken(SQLstr):
    conn=cx_Oracle.connect('MOBILEABPP/MOBILEABPP@TSTMDM') 
    c=conn.cursor()
    #x=c.execute("Insert into MOBILEABPP.PRODUCT_INFO(ID, NAME, PRICE, RANK, ONSALE_DATE, NETWORK_TYPE, FOURG_NET, MAINSCREENSIZE, CPU_TYPE, CPU_NAME, BATTERY, CAMERA, OS)Values('1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1')")
    resp=c.execute(SQLstr)
    c.execute("commit")
    #INSTER INTO PRODUCT_INFO
    #print x.fetchall()[2][1]
    c.close()
    conn.close() 
    return  resp
    