'''
Created on 2019-12-19

@author: wuqi2
'''

import cx_Oracle
from _random import Random
# import Random
import random
from django.db.models.functions.base import Substr

def dbModify(SQLstr):
    conn=cx_Oracle.connect('PCGSDC/PCGSDC@TSTCSEN') 
    c=conn.cursor()
    #x=c.execute("Insert into MOBILEABPP.PRODUCT_INFO(ID, NAME, PRICE, RANK, ONSALE_DATE, NETWORK_TYPE, FOURG_NET, MAINSCREENSIZE, CPU_TYPE, CPU_NAME, BATTERY, CAMERA, OS)Values('1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1')")
    SQLstr = SQLstr.replace(u'\xae',u' ')
    SQLstr =SQLstr.replace(u'\u2122',u' ')
#     SQLstr = SQLstr.replace(u'\xa0',u' ')
    print(SQLstr)
    resp=c.execute(SQLstr)
    x=c.execute("commit")
    #INSTER INTO PRODUCT_INFO
    #print x.fetchall()[2][1]
    c.close()
    conn.close() 
    return  resp

def dbSelect(SQLstr):
    conn=cx_Oracle.connect('PCGSDC/PCGSDC@TSTCSEN') 
    c=conn.cursor()
    x=c.execute("Insert into MOBILEABPP.PRODUCT_INFO(ID, NAME, PRICE, RANK, ONSALE_DATE, NETWORK_TYPE, FOURG_NET, MAINSCREENSIZE, CPU_TYPE, CPU_NAME, BATTERY, CAMERA, OS)Values('1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1')")
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




def getsql1(ASN):
    SQLstr='''
    INSERT INTO z_ui_odm_asn_gr (
    status,
    vbeln,
    verur,
    asn_line,
    matnr,
    lfimg,
    anzpk,
    uint_price,
    btgew,
    ntgew,
    coo,
    lifnr,
    odm_pn,
    odm_po,
    odm_po_line,
    invoice_number,
    ship_to
) VALUES (
    'NEW',
    'test',
    '800001'''
    SQLstr=SQLstr+ASN+'''',
    1,
    'SW10A11511',
    10,
    '11',
    10,
    5.1,
    4.911,
    'CHINA',
    'SH00010001',
    'PK32000AR90',
    '6200283961',
    '10',
    'Invoice001',
    '1010066619'
)'''
    return (SQLstr)

def getsql2(ASN):
    SQLstr='''
INSERT INTO z_ui_odm_asn_gr (
    status,
    vbeln,
    verur,
    asn_line,
    matnr,
    lfimg,
    anzpk,
    uint_price,
    btgew,
    ntgew,
    coo,
    lifnr,
    odm_pn,
    odm_po,
    odm_po_line,
    invoice_number,
    ship_to
) VALUES (
    'NEW',
    'test',
    '800001'''
    SQLstr=SQLstr+ASN+'''',
    2,
    'SW10H24504',
    11,
    '12',
    20,
    6.1,
    5.911,
    'TAIWAN',
    'SH00010001',
    'PK32000EP90',
    '6200283962',
    '10',
    'Invoice002',
    '1010066619'
)'''
    return SQLstr
def getsql3(ASN):
    SQLstr='''INSERT INTO z_ui_odm_asn_gr (
    status,
    vbeln,
    verur,
    asn_line,
    matnr,
    lfimg,
    anzpk,
    uint_price,
    btgew,
    ntgew,
    coo,
    lifnr,
    odm_pn,
    odm_po,
    odm_po_line,
    invoice_number,
    ship_to
) VALUES (
    'NEW',
    'test',
    '800001'''
    SQLstr=SQLstr+ASN+'''',
    3,
    'SW10H24486',
    12,
    '13',
    30,
    7.1,
    6.911,
    'CHINA',
    'SH00010001',
    'PK32000EP50',
    '6200283963',
    '10',
    'Invoice003',
    '1010066619'
)
'''
    return SQLstr


loop =1
while loop<=1000:
        ASN= "%04d" % loop
#         Linecount = random.randrange (1,2,1)
#         curr_line=1
        print (ASN)
        
        SQL =getsql1(ASN);
        print(SQL)
        dbModify(SQL);
        
        SQL =getsql2(ASN);
        print(SQL)
        dbModify(SQL);
        
        SQL =getsql3(ASN);
        print(SQL)
        dbModify(SQL);
        
#         while curr_line <= Linecount:
#             ASN_LINE= "%05d" % curr_line 
#             print (ASN,ASN_LINE) 
#             
#             SQL =getsql(ASN,ASN_LINE);
#             
#             print(SQL)
#             
#             curr_line=curr_line+1
        
        loop=loop+1
            
        

# SQLstr='''
#     INSERT INTO z_ui_odm_asn_gr (
#     vbeln,
#     posnr,
#     erdat,
#     lfart,
#     verur,
#     btgew,
#     ntgew,
#     gewei,
#     anzpk,
#     lifnr,
#     wadat_ist,
#     matnr,
#     werks,
#     lgort,
#     vgbel,
#     vgpos,
#     lfimg,
#     bwart,
#     category_sn,
#     sernr,
#     parts_type,
#     uint_price,
#     ship_to,
#     odm,
#     tpl_receipt_id,
#     time_zone,
#     supplier_id,
#     ship_to_id,
#     receipt_date,
#     tpl_receipt_line_id,
#     item_id,
#     invoice_number,
#     dest_storage_location,
#     po_number,
#     po_line_id,
#     gr_type,
#     qty,
#     delivery_notes,
#     hawb,
#     status,
#     reason,
#     sys_created_by,
#     sys_created_date,
#     sys_modified_by,
#     sys_modified_date,
#     status_show,
#     coo,
#     site_name,
#     odm_pn,
#     odm_po,
#     odm_po_line,
#     status_gr,
#     asn_line,
#     vmi_id
# ) VALUES (
#     'test',
#     '000001',
#     '20191022',
#     'EL',
#     '807105879',
#     0,
#     0,
#     NULL,
#     '00005',
#     '1000019724',
#     '00000000',
#     'SSA0T09104',
#     'H000',
#     NULL,
#     '7514037662',
#     '000010',
#     220,
#     NULL,
#     'ASN',
#     NULL,
#     'COMPONENT',
#     170.1,
#     '1010001545',
#     NULL,
#     NULL,
#     NULL,
#     NULL,
#     NULL,
#     NULL,
#     NULL,
#     NULL,
#     '6666666666',
#     NULL,
#     '6666',
#     NULL,
#     NULL,
#     2,
#     NULL,
#     NULL,
#     'NEW',
#     NULL,
#     'manual',
#     SYSDATE,
#     NULL,
#     SYSDATE,
#     'ACTIVE',
#     'CN',
#     NULL,
#     NULL,
#     NULL,
#     NULL,
#     NULL,
#     NULL,
#     NULL
# )
# '''
# dbModify(SQLstr)
