# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 17:22:34 2015

@author: z3185971
"""

import matplotlib.pyplot as plt
import numpy as np

from useful_functions import *
from ImportQSSFiles import *


min_f = 0
max_f = 0
gain = 9
rel_amp = 0 #relative amplitude of sin wave compared to the DC offset
period = 1 #s
delay = 0 #s
offset_calc_time = 0 #s - The absolute time before the delay to include data in the calculation of the DC offset 
num_repeats = 1 # number of repeated measurements per individual setting
amplifier = 'Femto'
cap = '_OC'

# RB1 parameters
channel = 'PC' # the channel to analyse
# Femto parameters
HorL = 'L' # what setting to use on the voltage pre-amp



Load = LoadData()
Load.Directory = 'H:/DATA/20150709 Amp re-testing/' + amplifier + '/Noise/'
#Load.Directory = '/Users/Bob/Dropbox/PhD/Code/Sample data/'
for repeat in range(1,num_repeats+1):
    
    
    Load.RawDataFile = amplifier + '_Gain '+ str(gain) + '_Amp ' + str(rel_amp) + ' rel_Period ' + str(period) + 's_0 freqs_From '+ str(min_f) + ' to ' + str(max_f) + '-' + str(repeat) + cap +'.Raw Data.dat'
    
    #Load.RawDataFile = 'Femto_GND_FBW_DC_' + str(HorL) + '_Gain '+ str(gain) + '_Amp ' + str(rel_amp) + ' rel_Period ' + str(period) + 's_10 freqs_From '+ str(min_f) + ' to ' + str(max_f) + '-' + str(repeat) + '.Raw Data.dat'
    
    Data = Load.Load_RawData_File()


    print Data.shape
    # 
    plt.plot(Data['Time'],Data[channel],'.')
    #plt.show()
    #plt.plot(Data['Time'],Data[channel],'-')
    #plt.xlim(0.2,0.21)
    plt.show()
    
    Data[channel] = -1*Data[channel]
     # 
    plt.plot(Data['Time'],Data[channel],'.')
    #plt.show()
    #plt.plot(Data['Time'],Data[channel],'-')
    #plt.xlim(0.2,0.21)
    plt.show()
    
    Do_FFT(Data[channel], Data[1]['Time']-Data[0]['Time'],10**min_f,10**max_f,rel_amp)