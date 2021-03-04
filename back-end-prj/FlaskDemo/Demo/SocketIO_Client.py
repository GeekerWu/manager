'''
Created on 2019-10-16

@author: wuqi2
'''

import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

# sio.connect('http://localhost:8888')
sio.connect('http://10.112.24.199:8888')
sio.wait()