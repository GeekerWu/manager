'''
Created on 2019-10-16

@author: wuqi2
'''


from threading import Lock
from flask import Flask 
from flask_cors import CORS
from flask_socketio import SocketIO,emit

import time
from time import sleep
# from concurrent.futures import ThreadPoolExecutor
import cx_Oracle
from alembic.command import init
from _overlapped import NULL
from _datetime import date
from astropy.io.ascii.tests.test_ecsv import data


import random


app = Flask(__name__)
# app_cors=CORS(app)
# monitor_task = ThreadPoolExecutor(1)
socketio = SocketIO(app,cors_allowed_origins='*')
# socketio.init_app(app)

global run
run='running'
thread = None
def random_data():
    data_list=['Green','Red','Yellow','Blue','Black','White']
    ydata = random.randrange(20, 50, 1)
    xdata = data_list[random.randrange(0, 5, 1)]
    return {'xdata':xdata,'ydata':ydata}





def schedule_check():
    last_dml=''
#         print(f'status is {self.status}')
    checkfreq = 8
    conn=cx_Oracle.connect('PCGSDC/PCGSDC@TSTCSEN') 
    c=conn.cursor() 
    
    while run=='running':
#             curr_size = len(blockchain.current_transactions)
#             print(f'current transaction size is: {curr_size}')
#             if curr_size > trans_size:
#                 print(f'sent mine request')
#                 requests.get(f'{masterloc}/mine')
        sqlstr='''
            select to_char(scn_to_timestamp(max(ora_rowscn)),'yyyy-mm-dd hh24:mi:ss') as lats_dml_time from Z_UI_RESEND_REQUEST
        '''
        res=c.execute(sqlstr)
        max_dml=res.fetchone()[0]
        if last_dml=='':
            print('first asign')
            last_dml=max_dml
        elif last_dml==max_dml:
            print('same data')
            socketio.emit('response',{'msg':'same data'},namespace='/test')
            
            randData=random_data()
            socketio.emit('refreshdata',randData,namespace='/test')
            
        else:
            print('data change')
            last_dml=max_dml
            socketio.emit('response',{'msg':'data change'},namespace='/test')
#                 with app.app_context():
#                      socketio.emit('response')               
#         print('schedule check')
       
        socketio.sleep(checkfreq)
        
    else:
        x_old=[]
        c.close()
        conn.close() 
        print('schedule check stop')
    
#     def schedule_stop(self):
#         self.status=''

    
# # @socketio.on('request_for_response',namespace='/test')
# @socketio.on('serverEventMessage',namespace='/test')
# def give_response(data):
#     print('request_for_response calling from client')
#     value = data.get('param')
#     print(value)
#     if value=='realtimestart':
#        print('new process')
#        emit('response',{'code':'200','msg':'schedule start'})
# #        t = threading.thread(target=schedule_check('running'), name='schedule_check',daemon=True)
# #        t.start()
#        task=socketio.start_background_task(schedule_check())
#        print('schedule ',run)
#        emit('response',{'code':'200','msg':'schedule start222'})
# #        emit('response',{'code':'200','msg':'schedule start'})
#     elif value=='realtimestop':
#        
#        print('schedule ',run)
#        emit('response',{'code':'200','msg':'schedule stop'})
#     else:
#         print(data)
#     #进行一些对value的处理或者其他操作,在此期间可以随时会调用emit方法向前台发送消息
# #     time.sleep(1)
# #     emit('server sent',{'code':'200','msg':'processed'})
# # @socketio.on('connect',namespace='/test')
@socketio.on('subscribe',namespace='/test')
def subscribe(data):
    print('request_for_client calling from client',data)
#     socketio.
#     if task ='':
    global thread
    if thread is None:
#         print('Task is not run init a new task')
        thread=socketio.start_background_task(schedule_check)
        print(thread)
    else:
        print('thread already run')
    print('done')



@socketio.on('connect')
def connect():
    print('connect ')
    print('sent response')
    emit('response',{'code':'200','msg':'connected'},namespace='/test')
#     task=socketio.start_background_task(schedule_check())
#     time.sleep(5)
#     emit('message',{'code':'200','msg':'hahahha'})
#     print('sid ',sid)
#     print('environ ',environ)

@socketio.on('disconnect',namespace='/test')
def disconnect():
    print('disconnect ')
    emit('response',{'code':'200','msg':'disconnect'})
#     print('sid ',sid)
#     print('environ ',environ)
     


"""
对app进行一些路由设置
"""
"""
对socketio进行一些监听设置
"""

if __name__ == '__main__':
    socketio.run(app,debug=True,host='0.0.0.0',port=8888)
