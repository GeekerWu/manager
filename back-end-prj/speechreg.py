import speech_recognition as sr
import os
from aip import AipSpeech
from playsound import playsound
#import pygame
import ffmpeg
import wave
import time

#------analysis baidu-----
#from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '23742613'
API_KEY = 'ZgZG4EDvfBcCKAYzYOl6u4BQ'
SECRET_KEY = 'Rd7PwMXXFK2mhnV99Qt2QjY2HAGRPuvN'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result = client.synthesis('干嘛呢？', 'zh', 1, {
'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
# play mp3 file
#support rasp
# os.system('mplayer %s' % 'audio.mp3')
#support windows
playsound('audio.mp3')
try:
    os.remove('audio.mp3')
except IOError:
    print('Warning: 没有找到文件或读取文件失败')


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# # write audio to a RAW file
# with open("microphone-results.raw", "wb") as f:
#     f.write(audio.get_raw_data())

# write audio to an AIFF file
# with open("microphone-results.aiff", "wb") as f:
#     f.write(audio.get_aiff_data())

# # write audio to a FLAC file
# with open("microphone-results.flac", "wb") as f:
#     f.write(audio.get_flac_data())

# write audio to a WAV file
# with open("C:\\Users\\GeekerWu\\Desktop\\manager\\back-end-prj\\microphone-results.wav", "wb") as f:
#save audio file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())
    print("file saved")
#remove 16000hz audio file
try:
    os.remove('microphone-results16000.wav')
except IOError:
    print('Warning: 没有找到文件或读取文件失败')


#convert new audio file
#import ffmpeg
ffmpeg.input('microphone-results.wav').output('microphone-results16000.wav', ar=16000).run()

#print audio info
#import wave
wavFile = r"microphone-results16000.wav"
f = wave.open(wavFile)
# 音频头 参数
params = f.getparams()
Channels = f.getnchannels()
SampleRate = f.getframerate()
bit_type = f.getsampwidth() * 8
frames = f.getnframes()
Duration = frames / float(SampleRate)  # 单位为s

print("音频头参数：", params)
print("通道数(Channels)：", Channels)
print("采样率(SampleRate)：", SampleRate)
print("比特(Precision)：", bit_type)
print("采样点数(frames)：", frames)
print("帧数(Duration)：", Duration)




# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
# 识别本地文件
result = client.asr(get_file_content('microphone-results16000.wav'), 'wav', 16000, {
    'dev_pid': 1537,
})
#print resule
print(result)
print(result['result'][0])
if(result['result'][0]=='你好啊！'):
    speechstr='你也好啊！'
elif(result['result'][0]=='明天星期几啊？'):
    speechstr='我也不知道啊，哈哈哈哈哈'
else:
    speechstr=result['result'][0]
# using baidu generate mp3 file
#result = client.synthesis(result['result'][0], 'zh', 1, {
#    'vol': 5,
#})

result = client.synthesis(speechstr, 'zh', 1, {
    'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
# play mp3 file
#support rasp
# os.system('mplayer %s' % 'audio.mp3')
#support windows
playsound('audio.mp3')

#filepath = r'audio.mp3';
#pygame.mixer.init()
# 加载音乐
#pygame.mixer.music.load(filepath)
#pygame.mixer.music.play(start=0.0)
#播放时长，没有此设置，音乐不会播放，会一次性加载完
#time.sleep(300)
#pygame.mixer.music.stop()














#------analysis local-----
# time.sleep(2)
# print('analysis')
# # test = sr.AudioFile("C:\\Users\\GeekerWu\\Desktop\\manager\\back-end-prj\\microphone-results.wav")
# test = sr.AudioFile("microphone-results.wav")
# with test as source:
#     audio = r.record(source)
# type(audio)
# c=r.recognize_sphinx(audio, language='en-US')     #识别输出
# #c=r.recognize_sphinx(audio, language='zh-cn')     #识别输出
# print(c)


#---------speech local
# time.sleep(2)
# print('py saying')
# import pyttsx3
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)
#
# voices = engine.getProperty('voices')
# for voice in voices:
#     print(voice)
#
#
# # 设置当前的属性值engine.setProperty('voice', voice.id)
# # 获取当前的属性值engine.getProperty('voice')
# # 声音属性（音色处理）
# # engine.setProperty('voice', voice.id)
# # 语速属性（赫兹处理）
# # engine.setProperty('rate', rate-150)
# # 音量大小
#
#
#
# # engine.setProperty('voice','zh')
#
#
# # engine.say('hello world')
# if c == '利好':
#     engine.say('大家好，才是真的好')
#     engine.runAndWait()
# elif c == '你 好':
#     engine.say('大家好，才是真的好')
#     engine.runAndWait()
# elif c == '你好':
#     engine.say('大家好，才是真的好')
#     engine.runAndWait()
# else:
#
#     # time.sleep(2)
#     # engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0')
#     #
#     # engine.say('我是灰灰')
#     # time.sleep(2)
#     # engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0')
#     #
#     # engine.say('ハルカです')
#     # time.sleep(2)
#     # engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
#     #
#     # engine.say('I am ZIRA')
#     # time.sleep(2)
#     # engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-TW_HANHAN_11.0')
#
#     #engine.say('speaking from raspberry')
#     engine.setProperty('voice', 'Mandarin')
#     engine.say('你好')
#     engine.runAndWait()

