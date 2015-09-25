# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:09:47 2015

Code to analyse real signals produced using make_log_noise() 
Assumes that the signal comes with delay s gap at the front, period seconds of real signal, 
and then trailing zeros.

Adjust the input parameters and file paths to perform the analysis
@author: z3185971
"""

import matplotlib.pyplot as plt
import numpy as np

from useful_functions import *
from ImportQSSFiles import *


min_f = 4
max_f = 5
gain = 3
rel_amp = 0.05 #relative amplitude of sin wave compared to the DC offset
period = 0.1 #s
delay = 0.104 #s
offset_calc_time = 0.01 #s - The absolute time before the delay to include data in the calculation of the DC offset 
num_repeats = 1 # number of repeated measurements per individual setting
amplifier = 'Femto'

# RB1 parameters
channel = 'PC' # the channel to analyse
# Femto parameters
HorL = 'L' # what setting to use on the voltage pre-amp



Load = LoadData()
Load.Directory = 'H:/DATA/20150709 Amp re-testing/' + amplifier + '/Gain ' + str(gain) + '/'
#Load.Directory = '/Users/Bob/Dropbox/PhD/Code/Sample data/'
for repeat in range(1,num_repeats+1):
    
    
    Load.RawDataFile = amplifier + '_Gain '+ str(gain) + '_Amp ' + str(rel_amp) + ' rel_Period ' + str(period) + 's_10 freqs_From '+ str(min_f) + ' to ' + str(max_f) + '-' + str(repeat) + '.Raw Data.dat'
    
    #Load.RawDataFile = 'Femto_GND_FBW_DC_' + str(HorL) + '_Gain '+ str(gain) + '_Amp ' + str(rel_amp) + ' rel_Period ' + str(period) + 's_10 freqs_From '+ str(min_f) + ' to ' + str(max_f) + '-' + str(repeat) + '.Raw Data.dat'
    
    Data = Load.Load_RawData_File()
    
    #==============================================================================
    # print Data[0:3]
    print Data.shape
    # 
    plt.plot(Data['Time'],Data[channel],'.')
    # 
    plt.xlim(delay-offset_calc_time,delay)
    #plt.show()
    #plt.plot(Data['Time'],Data[channel],'-')
    #plt.xlim(0.2,0.21)
    plt.show()
    #==============================================================================

    #test code for the time step issue
    #time_test = np.zeros_like(Data['Time'])
    #for i in range(0,248399 - 1):
    #    time_test[i] = Data[i+1]['Time']-Data[i]['Time']
    #plt.plot(time_test, '.')
    #plt.show()
    ######################
   
    
    # Calculate the DC_offset
    DC_offset = np.mean(Data[ np.logical_and(Data['Time'] > (delay - offset_calc_time), Data['Time'] < delay)][channel], axis=0)
    
    print DC_offset
    
    # Delete the first 0.1s
    Data =  np.delete(Data,np.where(Data['Time']< delay),0)
    
    # Delete trailing zeros
    Data = np.delete(Data,np.where(Data['Time'] > (delay + period)),0)
    
    
    
    print Data.shape
    
    plt.plot(Data['Time'],Data[channel],'-')
    plt.title('Raw signal - ' + channel + '. Repeat #' + str(repeat), fontweight='bold')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.show()
    
    # Convert to relative scale. Now the unattenuated amplitude should be the same as the relative amplitude that was input
    Data[channel] = np.divide(Data[channel],DC_offset)    
    
    plt.plot(Data['Time'],Data[channel],'-')
    plt.title('Raw signal (relative scale) - ' + str(channel), fontweight='bold')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.show()
    
    ###############################    
    #code to test redistributing with an even timebase
    
    #new_timestep = 0.000001
    #new_x = np.linspace(delay,delay+period,period/new_timestep)
    #new_y = np.interp(new_x,Data['Time'],Data[channel])
    
    #plt.plot(new_x,new_y, '-')
    #plt.show()    
    
    #Do_FFT(new_y, new_x[1]-new_x[0],10**(max_f+1))
    ##############################
    #yf = np.fft.rfft(Data[channel])
    #print 'done rfft'
    #yf = np.fft.fft(Data[channel])
    #print 'done fft'
    Do_FFT(Data[channel], Data[1]['Time']-Data[0]['Time'],10**min_f,10**max_f,rel_amp)

