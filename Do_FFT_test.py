# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 14:04:13 2015
Test code for Do_FFT()
@author: z3185971
"""

from useful_functions import *
import matplotlib.pyplot as plt
import numpy as np



freq1 = 5 #Hz
freq2 = 6 #Hz
num_freqs = 10
amp1 = 0.05
#amp2 = 1.0
#phase1 = 13 #deg
#phase2 = 90 #deg
period = 0.1 #s
sample_rate = 1200000.00 #Hz
time_step = 1 / sample_rate

x = np.linspace(0.0, period, period*sample_rate)

#y1 = my_sin(amp1,freq1,phase1,x) + my_sin(amp2,freq2,phase2,x)
#y2 = make_lin_noise(5,10,1,x)
y3 = make_log_noise(freq1,freq2,num_freqs,amp1,x)




plt.plot(x,y3, '.-')
plt.title('Input function',fontweight='bold')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (a.u.)')
plt.show()
#plt.plot(x,y2)
#plt.show()
Do_FFT(y3,x[1]-x[0],10**freq1,10**freq2,amp1)


