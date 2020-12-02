import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685(0x40)
pwm2 = Adafruit_PCA9685.PCA9685(0x41)
def set_servo_angle(channel, angle):
    date=4096*((angle*11)+500)/20000
    date=int(4096*((angle*11)+500)/(20000)+0.5)
    print(date)
    if channel<=15:
        pwm.set_pwm(channel, 0, date)
    elif channel>15 and channel<32:
        channel=channel-16
        pwm2.set_pwm(channel, 0, date)
    #pwm.set_pwm(channel, 0, date)
print('Moving servo on channel x, press Ctrl-C to quit...')  
while True:  
    # Move servo on channel O between extremes.  
    channel=int(input('pleas input channel:'))
    #channel=0
    angle=int(input('pleas input angle(best30-200):'))  
    set_servo_angle(channel, angle)  
