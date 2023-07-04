#!/usr/bin/env python
#
# *********     Sync Write Example      *********
#
#
# Available SCServo model on this example : All models using Protocol SCS
# This example is tested with a SCServo(SCS), and an URT
#

import sys
import os

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
from scservo_sdk import *                      # Uses SCServo SDK library

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
    print("Press read or write to continue! (or press ESC to quit!)")
    operation=input('please in put \'w\'to write, \'r\' to read ')
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
        '''
        if moving == 0:
            print('status not moveing')
        '''
    '''
    for scs_id in range(1, 11):
        # Add SCServo#1~10 goal position\moving speed\moving accc value to the Syncwrite parameter storage
        scs_addparam_result = packetHandler.SyncWritePos(scs_id, scs_goal_position[index], 0, SCS_MOVING_SPEED)
        if scs_addparam_result != True:
            print("[ID:%03d] groupSyncWrite addparam failed" % scs_id)

    # Syncwrite goal position
    scs_comm_result = packetHandler.groupSyncWrite.txPacket()
    if scs_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(scs_comm_result))

    # Clear syncwrite parameter storage
    packetHandler.groupSyncWrite.clearParam()

    # Change goal position
    if index == 0:
        index = 1
    else:
        index = 0
    '''
# Close port
portHandler.closePort()
