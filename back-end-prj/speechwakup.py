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
'''
def saying(str):
    result = client.synthesis(str, 'zh', 1, {
    'vol': 5,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)
    # play mp3 file

    try:#support rasp
        os.system('mplayer %s' % 'audio.mp3')
        #support windows
        #playsound('audio.mp3')
        os.remove('audio.mp3')
    except IOError:
        print('Warning: 没有找到文件或读取文件失败')

saying('说点什么')
'''
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
'''
saying('原音为')
#os.system('mplayer %s' % 'microphone-results.wav')
#playsound('microphone-results.wav')
saying('转换后为')
#os.system('mplayer %s' % 'microphone-results16000.wav')
#playsound('microphone-results16000.wav')
'''



#------analysis local-----
time.sleep(2)
print('analysis')
r = sr.Recognizer()
# test = sr.AudioFile("C:\\Users\\GeekerWu\\Desktop\\manager\\back-end-prj\\microphone-results.wav")
test = sr.AudioFile("microphone-results16000.wav")
with test as source:
    audio = r.record(source)
type(audio)
#en=r.recognize_sphinx(audio, language='en-US')     #识别输出
zh=r.recognize_sphinx(audio, language='zh-cn')     #识别输出
#print(en)
print(zh)
playsound('microphone-results16000.wav')
#saying('识别后为'+c)



#---------speech local
time.sleep(2)
print('py saying')
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
#
voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
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

    # 设置当前语音声音为女性，当前声音不能读中文
#    engine.setProperty('voice', voices[1].id)
    # 设置当前语音声音为男性，当前声音可以读中文
 #   engine.setProperty('voice', voices[0].id)

engine.setProperty('voice',voices[0].id)
#
#
voice = engine.getProperty('voice')
print(f'语音声音：{voice}')
engine.say(zh)
engine.runAndWait()
engine.stop()
# 保存音频
engine.save_to_file('张三，王五，你们好，请离开！', filename='go_out.wav', name='test')
engine.runAndWait()

#engine.say(zh)
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

