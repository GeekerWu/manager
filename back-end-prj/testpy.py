'''from playsound import playsound
from aip import AipSpeech
""" 你的 APPID AK SK """
APP_ID = '26613765'
API_KEY = 'iXu23BlBS9fLq6P3QOi0qDtj'
SECRET_KEY = '6C0QBKuwKTyfu4vBnpNVHYDPs4iMZsdT '
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result = client.synthesis('哈哈哈哈','zh', 1, {'vol': 5,})
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
# play mp3 file
playsound("audio.mp3")
#support rasp
#os.system('mplayer %s' % 'audio.mp3')
'''
import os
#from playsound import playsound
import librosa
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from playsound import playsound
import numpy as np
#import ffmpeg
import time
print('record 2 second sound')
#suopport raspberry
#os.system('arecord -D "plughw:2,0" -f dat -c 1 -r 22500 -d 5 test2.wav')
#support windows
fs = 44100  # Sample rate
seconds = 2  # Duration of recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('test.wav', fs, myrecording)  # Save as WAV file


print('play orignal sound')
time.sleep(4)
#support  windows
playsound('test.wav')
#support raspberry
#os.system('mplayer %s' % 'test2.wav')

#ffmpeg.input('test2.wav').output('test2.mp3', ar=16000).run()

y,sr=librosa.load('test.wav')
y50=librosa.resample(y=y, orig_sr=sr, target_sr=5)
print(y50)
#sf.write('test50.wav',y,50)

'''
print('play X2 speed sound')
time.sleep(4)
# playingspeed
librosa.output.write_wav('test2X2.wav',y,sr*2)
os.system('mplayer %s' % 'test2X2.wav')
'''

'''
# pinch
print('play pinch sound')
time.sleep(4)
b=librosa.effects.pitch_shift(y,sr,n_steps=14)
sf.write('test2shift14.wav',b,sr)
os.system('mplayer %s' % 'test2shift14.wav')
'''
'''
#stft
a=librosa.stft(y)
length=len(a)
# do some change make sound effect
r_a=a[10:length-10]

#isft
b=librosa.istft(r_a)
print('play stft sound')
time.sleep(4)
sf.write('test2stft.wav',b,sr)
os.system('mplayer %s' % 'test2stft.wav')
'''
#plt
fig=plt.figure()
s1=fig.add_subplot(2,1,1)
s2=fig.add_subplot(2,1,2)
#s3=fig.add_subplot(3,1,3)

s1.plot(y)
s2.plot(y50)
#s3.plot(b)
plt.show()
