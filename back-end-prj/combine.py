import sox
cbn = sox.Combiner()
# pitch shift combined audio up 3 semitones
cbn.pitch(3.0)
# convert output to 8000 Hz stereo
cbn.convert(samplerate=16000, n_channels=1)
# create the output file
cbn.build(['output1.wav','output2.wav'], 'output555.wav', 'concatenate')




