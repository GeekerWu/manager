import os

from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()
#C:\ProgramData\Anaconda3\envs\back-end-prj\lib\site-packages\pocketsphinx\model
#print(model_path)
#support us
speech = LiveSpeech(
verbose=False,
sampling_rate=16000,
buffer_size=2048,
no_search=False,
full_utt=False,
hmm=os.path.join(model_path, 'en-us'),
lm=os.path.join(model_path, 'en-us.lm.bin'),
dic=os.path.join(model_path, 'cmudict-en-us.dict')
)
'''
#support ch
speech = LiveSpeech(
verbose=False,
sampling_rate=16000,
buffer_size=2048,
no_search=False,
full_utt=False,
hmm=os.path.join(model_path, 'zh/zh_broadcastnews_16k_ptm256_8000'),
lm=os.path.join(model_path, 'zh/zh_broadcastnews_64000_utf8.DMP'),
dic=os.path.join(model_path, 'zh/zh_broadcastnews_utf8.dic')
)
'''

for phrase in speech:
    print("phrase:", phrase)
    print(phrase.segments(detailed=True))