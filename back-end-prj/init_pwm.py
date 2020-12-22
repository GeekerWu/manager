import Adafruit_PCA9685
import time
pwm = Adafruit_PCA9685.PCA9685(0x40)
pwm2 = Adafruit_PCA9685.PCA9685(0x41)
pwm3 = Adafruit_PCA9685.PCA9685(0x42)
def set_servo_angle(channel, date):
    #date=4096*((angle*11)+500)/20000
    #date=int(4096*((angle*11)+500)/(20000)+0.5)
    date=date*10
    print(channel,date)
    if channel<=5:
        time.sleep(1)
        pwm.set_pwm(channel, 0, date)
    elif channel>9 and channel<=15:
        
        time.sleep(1)
        pwm.set_pwm(channel, 0, date)
    elif channel>15 and channel<=31:
        channel=channel-16
        
        time.sleep(1)
        pwm2.set_pwm(channel, 0, date)

    elif channel > 31 and channel <= 48:
        channel = channel - 32

        time.sleep(1)
        pwm3.set_pwm(channel, 0, date)

    #pwm.set_pwm(channel, 0, date)
print('Moving servo on channel x, press Ctrl-C to quit...')  
while True:  
    # Move servo on channel O between extremes.  
    #channel=int(input('pleas input channel:'))
    #channel=0
    #angle=int(input('pleas input init angle(best50-200):'))
    #50-200 

    #80[50-170],60,95[60-140],120[50-170],120[80-170],90[60-160],mid,60[60-140],100[60-160],130[70-160],90[60-120],120[50-150],80[70-160]
    #for channel in [0,1,2,3,4,5,10,11,12,13,14,15]:
    #    set_servo_angle(channel, angle)
    channel=int(input('pleas input channel:'))  
    angle=int(input('pleas input angle:'))  
    set_servo_angle(channel, angle)      


