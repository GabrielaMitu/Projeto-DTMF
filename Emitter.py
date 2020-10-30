# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:21:35 2020

@author: gabri
"""

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift
from scipy import signal as window
from suaBibSignal import *

        
        
A = 1.5
fs = 44100
time = 1
t = np.linspace(-time/2, time/2, time*fs)

num = input("Escolha um número de 0 a 9: ")
hi_f = 0
lo_f = 0

if num == '1':
    hi_f = 1209
    lo_f = 697

    
elif num == '2':
    hi_f = 1336
    lo_f = 697

    
elif num == '3':
    hi_f = 1477
    lo_f = 697

    
elif num == 'A':
    hi_f = 1633
    lo_f = 697


elif num == '4':
    hi_f = 1290
    lo_f = 770

    
elif num == '5':
    hi_f = 1336
    lo_f = 770

    
elif num == '6':
    hi_f = 1477
    lo_f = 770

    
    
elif num == 'B':
    hi_f = 1633
    lo_f = 770

    
elif num == '7':
    hi_f = 1209
    lo_f = 852
    
    
elif num == '8':
    hi_f = 1336
    lo_f = 852

    
    
elif num == '9':
    hi_f = 1477
    lo_f = 852

    
    
elif num == 'C':
    hi_f = 1633
    lo_f = 852

    
    
elif num == 'X':
    hi_f = 1209
    lo_f = 941

    
elif num == '0':
    hi_f = 1336
    lo_f = 941

    
elif num == '#':
    hi_f = 1477
    lo_f = 941

    
elif num == 'D':
    hi_f = 1633
    lo_f = 941


x, ysin_1 = signalMeu().generateSin(lo_f, A, time, fs)

x2, ysin_2 = signalMeu().generateSin(hi_f, A, time, fs)

y = ysin_1 + ysin_2

sd.play(y)

#----- Cada frequência (alta e baixa) -------
plt.figure()
plt.xlim(0,time/200)
plt.plot(t,ysin_1,'r')
plt.plot(t,ysin_2,'b')
plt.grid()
plt.title('Frequências alta e baixa no tempo')


#------ Frequências somadas ---------

plt.figure()
plt.plot(t, y, 'r')
plt.xlim(0, time/60)
plt.grid()
plt.title('Frequências somadas no tempo')

