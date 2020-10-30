# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:13:53 2020

@author: gabri
"""

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift
from scipy import signal as window
from suaBibSignal import *
import pyaudio
import wave
import peakutils

A = 1.5
fs = 44100
time = 1
t = np.linspace(-time/2, time/2, time*fs)


DTMF_TABLE = {
    '1': [1209, 697],
    '2': [1336, 697],
    '3': [1477, 697],
    'A': [1633, 697],

    '4': [1209, 770],
    '5': [1336, 770],
    '6': [1477, 770],
    'B': [1633, 770],

    '7': [1209, 852],
    '8': [1336, 852],
    '9': [1477, 852],
    'C': [1633, 852],

    '*': [1209, 941],
    '0': [1336, 941],
    '#': [1477, 941],
    'D': [1633, 941],
} 

def compare_picos(lista_picos):
    
    for v in DTMF_TABLE.keys():
            l=0
            c=0
            t=DTMF_TABLE[v]
            coluna = t[0]
            linha=t[1]
            for x in lista_picos:
                if abs(coluna-x)<=10:
                    c = coluna
                if abs(linha-x)<=10:
                    l=linha
            if c!=0 and l!=0:
                print("high frequency: "+ str(c))
                print("low frequency: "+str(l))
                return v

#------ Record Audio ------

filename = "recorded.wav"
chunk = 1024
FORMAT = pyaudio.paInt16
channels = 1
sample_rate = 44100
record_seconds = 2
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=channels,
                rate=sample_rate,
                input=True,
                output=True,
                frames_per_buffer=chunk)
frames = []
print("Recording...")
for i in range(int(44100 / chunk * record_seconds)):
    data = stream.read(chunk)
    frames.append(data)
print("Finished recording.")
stream.stop_stream()
stream.close()
p.terminate()
wf = wave.open(filename, "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(sample_rate)
wf.writeframes(b"".join(frames))
wf.close()


#------ Algoritmo FFT -----

sd.default.samplerate = fs
sd.default.channels = 1
audio, samplerate = sf.read('recorded.wav')   # som gravado
yAudio = audio
samplesAudio = len(yAudio)
sd.play(audio)
sd.wait()


#------ Plot do sinal no tempo -----

plt.plot(yAudio)
plt.grid()
plt.title('Sinal no tempo')


#------ Obter transformada de Fourier -----

X, Y = signalMeu().calcFFT(yAudio, samplerate)
plt.figure("Fourier Audio")
plt.plot(X, np.abs(Y))
plt.grid()
plt.title('Fourier do Áudio')

    
p=0.9
n=0
picos=[]
while n<3:
    index = peakutils.indexes(np.abs(Y), thres=p, min_dist=100)
    n=0
    for freq in X[index]:
        n+=1
        if freq not in picos:
            picos.append(freq)
        p-=.06
print("freq de pico sao: {}" .format(str([x for x in picos]).strip('[]')))
        
print("Número escolhido: "+ str(compare_picos(picos)))

    