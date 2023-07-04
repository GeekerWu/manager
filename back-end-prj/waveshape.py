import wave
# 导入 wave 模块
import matplotlib.pyplot as plt
# 用于绘制波形图
import numpy as np
# 用于计算波形数据
import os

#  用于系统处理，如读取本地音频文件

f = wave.open(r"microphone-results16000.wav", 'rb')
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
print(framerate)

# 读取波形数据
strData = f.readframes(nframes)
# 将字符串转换为16位整数
waveData = np.frombuffer(strData, dtype=np.int16)
# 幅值归一化
waveData = waveData * 1.0 / (max(abs(waveData)))
# 计算音频的时间
time = np.arange(0, nframes) * (1.0 / framerate)

plt.plot(time, waveData)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Single channel 16000 wavedata")
plt.show()

f = wave.open(r"microphone-results.wav", 'rb')
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
print(framerate)

# 读取波形数据
strData = f.readframes(nframes)
# 将字符串转换为16位整数
waveData = np.frombuffer(strData, dtype=np.int16)
# 幅值归一化
waveData = waveData * 1.0 / (max(abs(waveData)))
# 计算音频的时间
time = np.arange(0, nframes) * (1.0 / framerate)

plt.plot(time, waveData)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Single channel 44100 wavedata")
plt.show()