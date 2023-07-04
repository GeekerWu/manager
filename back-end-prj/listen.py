import speech_recognition as sr
import os
from aip import AipSpeech
from playsound import playsound
import pyaudio
#import pygame
import ffmpeg
import wave
import time
import sox
from pathlib import Path



#------analysis baidu-----
#from aip import AipSpeech
AWAKE = 'false'
""" 你的 APPID AK SK """
APP_ID = '23742613'
API_KEY = 'ZgZG4EDvfBcCKAYzYOl6u4BQ'
SECRET_KEY = 'Rd7PwMXXFK2mhnV99Qt2QjY2HAGRPuvN'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
try:
    if os.path.exists('output1.wav'):
        os.remove('output1.wav')
    if os.path.exists('output2.wav'):
        os.remove('output2.wav')
    if os.path.exists('output3.wav'):
        os.remove('output3.wav')
    if os.path.exists('awake.txt'):
        os.remove('awake.txt')
    if os.path.exists('output.wav'):
        os.remove('output.wav')
except IOError:
    print('Warning: 没有找到文件或读取文件失败111')


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
        #os.system('mplayer %s' % 'audio.mp3')
        #support windows
        playsound('audio.mp3')
        os.remove('audio.mp3')

    except IOError:
        print('Warning: 没有找到文件或读取文件失败')

saying('start')


def record(filename,wavei):
    CHUNK = 512
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    # RATE = 44100
    RATE = 16000
    RECORD_SECONDS = 2
    WAVE_OUTPUT_FILENAME = filename

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("done")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    analysis(wavei)



#------analysis local-----
def analysis(i):
    # print('analysis')
    # print(filename)

    # create combiner
    cbn = sox.Combiner()
    # pitch shift combined audio up 3 semitones
    cbn.pitch(3.0)
    # convert output to 8000 Hz stereo
    cbn.convert(samplerate=16000, n_channels=1)
    # create the output file

    if i=='1':
        try:
            cbn.build(
                ['output3.wav', 'output1.wav'], 'output.wav', 'concatenate'
            )
        except:
            cbn.build(
                ['output0.wav', 'output1.wav'], 'output.wav', 'concatenate'
            )
    elif i=='2':
        try:
            cbn.build(
                ['output1.wav', 'output2.wav'], 'output.wav', 'concatenate'
            )
        except:
            cbn.build(
                ['output0.wav', 'output2.wav'], 'output.wav', 'concatenate'
            )
    elif i=='3':
        try:
            cbn.build(
                ['output2.wav', 'output3.wav'], 'output.wav', 'concatenate'
            )
        except:
            cbn.build(
                ['output0.wav', 'output3.wav'], 'output.wav', 'concatenate'
            )


    r = sr.Recognizer()
    # test = sr.AudioFile("C:\\Users\\GeekerWu\\Desktop\\manager\\back-end-prj\\microphone-results.wav")

    test = sr.AudioFile('output.wav')
    with test as source:
        audio = r.record(source)
    type(audio)
    try:
        c=r.recognize_sphinx(audio, language='en-US')     #识别输出
        #c=r.recognize_sphinx(audio, language='zh-cn')     #识别输出
        # if c=='hello':
    except:
        # print(filename, 'nothing saying')
        c=''

    if len(c):
        print('c', c)
        if 'hello' in c:
            fp = open("C:\\Users\\GeekerWu\\Desktop\\manager\\back-end-prj\\awake.txt",'w')
            fp.write(c)
            fp.close()
            saying('哈喽啊，啥事啊？')
            if os.path.exists('output1.wav'):
                os.remove('output1.wav')
            if os.path.exists('output2.wav'):
                os.remove('output2.wav')
            if os.path.exists('output3.wav'):
                os.remove('output3.wav')
            command()

def command():
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

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print("Say something!")
    # save audio file
    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())
        print("file saved")
    # remove 16000hz audio file
    try:
        os.remove('microphone-results16000.wav')
    except IOError:
        print('Warning: 没有找到文件或读取文件失败')

    # convert new audio file
    # import ffmpeg
    ffmpeg.input('microphone-results.wav').output('microphone-results16000.wav', ar=16000).run()

    # print audio info
    # import wave
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
    # print resule
    print(result)
    print(result['result'][0])
    if(result['result'][0]=='今天天气怎么样？'):
        saying('我也不知道，妇女就乐啊。哈哈哈哈')
    if os.path.exists('awake.txt'):
        os.remove('awake.txt')


        # saying('识别后为'+c)





# obtain audio from the microphone
while True:
        items = ['1', '2', '3']
        for i in items:
            #print(i)
            if os.path.exists('C:\\Users\\GeekerWu\\Desktop\\manager\\back-end-prj\\awake.txt'):
                print(os.path.exists('awake.txt'))
            else:
             # 不存在
                record('output' + i + '.wav',i)
            time.sleep(2)


        # r = sr.Recognizer()
        # with sr.Microphone() as source:
        # # print("Say something!")
        #     audio = r.listen(source)

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
        # save audio file
        # with open("microphone" + str(i) + ".wav", "wb") as f:
        #     f.write(audio.get_wav_data())
        #     print("file saved")
        # print(os.path.getsize("microphone" + str(i) + ".wav"))
        # convert("microphone" + str(i))







# def convert(filename):
#     print(filename)
#     #remove 16000hz audio file
#     try:
#         os.remove(filename+'16000.wav')
#     except IOError:
#         print('Warning: 没有找到文件'+filename+'16000.wav')
#     #convert new audio file
#     #import ffmpeg
#     ffmpeg.input(filename+'.wav').output(filename+'16000.wav', ar=16000).run()
#     try:
#         os.remove(filename + '.wav')
#     except IOError:
#         print('Warning: 没有找到文件' + filename + '.wav')
#     analysis(filename+'16000.wav')


    # saying('原音为')
    # os.system('mplayer %s' % 'microphone-results.wav')
    #playsound('microphone-results.wav')
    # saying('转换后为')
    # os.system('mplayer %s' % 'microphone-results16000.wav')
    #playsound('microphone-results16000.wav')




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

