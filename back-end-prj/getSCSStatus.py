#!/usr/bin/env python
#
# *********     Sync Write Example      *********
#   update servo status in Database input search
#   to get all alive servo write status in database
#
# Available SCServo model on this example : All models using Protocol SCS
# This example is tested with a SCServo(SCS), and an URT
#

import sys
import os
import pymysql

if os.name == 'nt':
    print('windows')
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

sys.path.append("..")
from SCServo_Python.scservo_sdk import *                      # Uses SCServo SDK library

# Default setting
BAUDRATE                    = 1000000           # SCServo default baudrate : 1000000
#DEVICENAME                  = '/dev/ttyUSB0'    # Check which port is being used on your controller
DEVICENAME                  = 'COM4'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

SCS_MINIMUM_POSITION_VALUE  = 10                # SCServo will rotate between this value
SCS_MAXIMUM_POSITION_VALUE  = 1000
SCS_MOVING_SPEED            = 2400              # SCServo moving speed

index = 0
scs_goal_position = [SCS_MINIMUM_POSITION_VALUE, SCS_MAXIMUM_POSITION_VALUE]         # Goal position

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Get methods and members of Protocol
packetHandler = scscl(portHandler)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    quit()


# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    quit()

while 1:
    #print("Press read or write to continue! (or press ESC to quit!)")

    operation=input('please in put \'w\'to write, \'r\' to read , \'s\' to status ')
    # operation = 's'
    if operation=='w':
        print('input w write operation')
        SCS_ID=int(input('SCS_ID:'))
        target_position=int(input('scs_goal_position:'))
        scs_comm_result, scs_error = packetHandler.WritePos(SCS_ID,target_position, 0, SCS_MOVING_SPEED)
        if scs_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(scs_comm_result))
        elif scs_error != 0:
            print("%s" % packetHandler.getRxPacketError(scs_error))

    elif operation=='r':
        print('input r read operation')
        SCS_ID = int(input('SCS_ID:'))
        # Read SCServo present position
        scs_present_position, scs_present_speed, scs_comm_result, scs_error = packetHandler.ReadPosSpeed(SCS_ID)
        if scs_comm_result != COMM_SUCCESS:
            print(packetHandler.getTxRxResult(scs_comm_result))
        elif scs_error != 0:
            print(packetHandler.getRxPacketError(scs_error))

        # Read SCServo moving status
        moving, scs_comm_result, scs_error = packetHandler.ReadMoving(SCS_ID)
        if scs_comm_result != COMM_SUCCESS:
            print(packetHandler.getTxRxResult(scs_comm_result))
        else:
            print("[ID:%03d] GoalPos:%d PresPos:%d PresSpd:%d Moving:%d" % (
            SCS_ID, scs_goal_position[index], scs_present_position, scs_present_speed,moving))
        if scs_error != 0:
            print(packetHandler.getRxPacketError(scs_error))

    elif operation == 's':
        # print('input s read status')
        # SCS_ID = int(input('SCS_ID:'))
        SCS_ID = int(1)
        # Read SCServo present position
        scs_present_load2b,datastring, scs_comm_result, scs_error = packetHandler.ReadLoad(SCS_ID)
        if scs_comm_result != COMM_SUCCESS:
            print(packetHandler.getTxRxResult(scs_comm_result))
        elif scs_error != 0:
            print(packetHandler.getRxPacketError(scs_error))
        else:
            # print("load is : 2b: %d " % (scs_present_load2b),datastring)
            moving, scs_comm_result, scs_error = packetHandler.ReadMoving(SCS_ID)
            if abs(scs_present_load2b) >60 and moving==0:
                scs_present_currp2b, scs_comm_result, scs_error = packetHandler.ReadCurrPosition(SCS_ID)
                target_position = scs_present_currp2b
                print("load is :  %d ，curr position is：  %d , moving flag is: %d" % (scs_present_load2b,target_position,moving))
                MOVING_SPEED = 10
                MOVING_STEP=5
                if scs_present_load2b>0 and scs_present_currp2b in range(100, 900, 1):
                    target_position=scs_present_currp2b+MOVING_STEP
                elif scs_present_load2b<0 and scs_present_currp2b in range(100, 900, 1):
                    target_position = scs_present_currp2b - MOVING_STEP
                if target_position not in range(100, 900, 1):
                    print('position out of rage')
                    if scs_present_load2b > 0:
                        target_position = scs_present_currp2b + 80
                    elif scs_present_load2b < 0:
                        target_position = scs_present_currp2b - 80
                    scs_comm_result, scs_error = packetHandler.WritePos(SCS_ID, target_position, 0, 400)
                    scs_comm_result, scs_error = packetHandler.WritePos(SCS_ID, 511, 0, 100)
                elif target_position >= 100 and target_position <= 900:
                    scs_comm_result, scs_error = packetHandler.WritePos(SCS_ID, target_position, 0, MOVING_SPEED)
                    # print(target_position)
    elif operation =='search':
        print('search')

        conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd='root',
            port=3306,
            db='ml',
            charset='utf8'
        )
        # 获取一个光标
        cursor = conn.cursor()
        for SCS_ID in range(1,55):
            # print(SCS_ID)

            scs_model_number, scs_comm_result, scs_error = packetHandler.ping(SCS_ID)
            if scs_comm_result == COMM_SUCCESS:
                print("[ID:%03d] ping Succeeded. SCServo model number : %d" % (SCS_ID, scs_model_number))

                scs_present_tmp1b, scs_comm_result, scs_error = packetHandler.ReadTmp(
                    SCS_ID)
                if scs_comm_result != COMM_SUCCESS:
                    print(packetHandler.getTxRxResult(scs_comm_result))
                elif scs_error != 0:
                    print(packetHandler.getRxPacketError(scs_error))
                else:
                    # print("temperature is :4b: %d 2b: %d 1b: %d" % (scs_present_tmp4b, scs_present_tmp2b, scs_present_tmp1b))
                    print("temperature is : %d" % (scs_present_tmp1b))

                scs_present_volt1b, scs_comm_result, scs_error = packetHandler.ReadVolt(
                    SCS_ID)
                if scs_comm_result != COMM_SUCCESS:
                    print(packetHandler.getTxRxResult(scs_comm_result))
                elif scs_error != 0:
                    print(packetHandler.getRxPacketError(scs_error))
                else:
                    # print("voltage is :4b: %d 2b: %d 1b: %d" % (scs_present_volt4b, scs_present_volt2b, scs_present_volt1b))
                    print("voltage is: %d" % (scs_present_volt1b))

                scs_present_load2b, datastring, scs_comm_result, scs_error = packetHandler.ReadLoad(SCS_ID)
                if scs_comm_result != COMM_SUCCESS:
                    print(packetHandler.getTxRxResult(scs_comm_result))
                elif scs_error != 0:
                    print(packetHandler.getRxPacketError(scs_error))
                else:
                     # print("load is: %d " % (scs_present_load2b))
                    moving, scs_comm_result, scs_error = packetHandler.ReadMoving(SCS_ID)
                    scs_present_currp2b, scs_comm_result, scs_error = packetHandler.ReadCurrPosition(SCS_ID)
                    target_position = scs_present_currp2b
                    print("load is :  %d ，curr position is：  %d , moving flag is: %d" % (scs_present_load2b, target_position, moving))
                    # 定义将要执行的SQL语句
                    # sql = "INSERT INTO servo_info (SERVOID, CURR_POSITION, SLOAD,VOLTAGE,TEMPERATURE) values (%s, %s, %s, %s, %s);"
                    sql = "INSERT INTO servo_info (SERVOID, CURR_POSITION, SLOAD,VOLTAGE,TEMPERATURE) values (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE CURR_POSITION=%s, SLOAD=%s, VOLTAGE=%s ,TEMPERATURE=%s;"
                    # SERVOID = SCS_ID
                    SERVOID,CURR_POSITION, LOAD, VOLTAGE, TEMPERATURE=SCS_ID,target_position,scs_present_load2b,scs_present_volt1b,scs_present_tmp1b
                    # 拼接并执行SQL语句
                    data =[SERVOID, CURR_POSITION, LOAD, VOLTAGE, TEMPERATURE, CURR_POSITION, LOAD, VOLTAGE, TEMPERATURE]
                    # data = [SERVOID, CURR_POSITION, LOAD, VOLTAGE, TEMPERATURE]
                    print(data)
                    cursor.execute(sql,data)

        # 涉及写操作注意要提交
        conn.commit()
        # 关闭连接
        cursor.close()
        conn.close()

        '''
            SERVOID
            NAME
            STATUS
            CURR_POSITION
            MINI_POSITION
            MAX_POSITION
            SPEED
            LOAD
            VOLTAGE
            TEMPERATURE
            MAXLOAD
            DESCRIPTION
            SERVOTYPE
            
            INSERT
                INTO
                table(id, name, age)
                values(1, 'yourname', 18)
                ON
                DUPLICATE
                KEY
                UPDATE
                name = 'yourname', age = 18;
            
            
        '''


        '''
            if scs_comm_result != COMM_SUCCESS:
                print("SSID %d %s" % (SCS_ID,packetHandler.getTxRxResult(scs_comm_result)))
            else:
                print("[ID:%03d] ping Succeeded. SCServo model number : %d" % (SCS_ID, scs_model_number))
            if scs_error != 0:
                print("SSID ERROR %d %s" % (SCS_ID,packetHandler.getRxPacketError(scs_error)))
        '''

            # portHandler.closePort()

# Close port
portHandler.closePort()
