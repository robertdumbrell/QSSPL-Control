# -*- coding: utf-8 -*-
"""
Created on Thu May 07 17:37:04 2015

@author: z3185971
"""
import numpy as np
import matplotlib.pyplot as plt



#==============================================================================
# def binning(data, binsize):
#     binnedData = np.zeros(2)    
#     print(binnedData)
# #    for i in xrange(0,data.shape[0]):
# #        if i % binsize == 0:
# #            np.append(binnedData, np.mean(data[i-binsize:i]))
#     return binnedData
#==============================================================================


def Bin_Data(data,BinAmount):
    #This is part of a generic binning class that Mattias wrote.
    #It lets binning occur of the first axis for any 2D or 1D array
        
    if BinAmount ==1:
        return data
    
    #Initialises
    if len(data.shape)==1:
        data2 = np.zeros((data.shape[0]//BinAmount))
    else:
        data2 = np.zeros((data.shape[0]//BinAmount,data.shape[1]))

        
    for i in range(data.shape[0]//BinAmount):
        data2[i] = np.mean(data[i*BinAmount:(i+1)*BinAmount],axis=0)

    return data2



def my_sin(amp, freq, phase, x):
    return amp * np.sin((freq * 2.0*np.pi*x) + (phase*(np.pi/180)))
    
    
    
def make_lin_noise(start_freq, end_freq, amp, x):
    
    if not start_freq < end_freq:
        print("Error in make_lin_noise: need to go from low to high frequency!")
    else:        
        
        y = np.zeros_like(x)
        
        for f in xrange(start_freq,end_freq+1):
            y = y + my_sin(amp,f,0,x)
        
        return y
    


def round_int_sig(x, sig):
    # iterates over each element in a numpy array and rounds to sig significant figures, assuming that each element is an integer
    # doesn't work for floating point arrays    
    print 'in sig fig rounding'
    for i in np.nditer(x, op_flags=['readwrite']):
        print i        
        i[...] = np.around(i, -1+sig-int(np.floor(np.log10(np.abs(i)))))
    
    print 'out of sig fig rounding'    
    return x
    
    
def make_log_noise(min_exponent, max_exponent, num_steps, amp, x):
    
    if not(min_exponent < max_exponent):
        print("Error in make_log_noise: need to go from low to high frequency!")
    
    elif max_exponent <= 2:
        frequencies = np.around(np.logspace(min_exponent, max_exponent, num=num_steps),0)
        print "Frequencies:"        
        print frequencies
    else:
        
        frequencies = round_int_sig(np.logspace(min_exponent, max_exponent, num=num_steps),2)
        print "Frequencies:"        
        print frequencies
    
    y = np.zeros_like(x)        
    for f in xrange(0,num_steps):
        y = y + my_sin(amp,frequencies[f],0,x)
        
    return y        
        

def Do_FFT(y,timestep,Min_freq,Max_freq,Max_amp):
    Peak_tolerance = 0.01    
    
    # Perform the FFT    
    yf = np.fft.fft(y)
    
    # Calculate the Amplitude
    yf_amp = 2*np.abs(yf)/y.size
    # Calculate the phase of each frequency component. We add 90 because we are 
    # inputting sine functions. These are on the y axis of the complex plane
    # so we want to measure the phase shift from the y axis.
    yf_phase = 90 + np.angle(yf, deg=True)
    print("The input data has %d discrete data points." % y.size)

    # Create the corresponding frequency domain for plotting the FFT   
    xf = np.fft.fftfreq(y.size, d=timestep)
    

    # Plot the real and imaginary parts of the transformed y's
    # Note that if the input signals are Sine curves then 0 phase shift 
    # results in a completely imaginary signal.
    #plt.plot(xf,yf.real/y.size,'g.-')
    #plt.plot(xf,yf.imag/y.size,'b.-')
    #plt.title("Real and imaginary parts of raw calculation", fontweight='bold')
    #plt.legend('RI')
    #plt.xlim(-Max_freq,Max_freq)
    #plt.semilogx()
    #plt.show()    
    
    # Plot the calculated amplitudes of the component frequencies
    plt.plot(xf,yf_amp,'r.')
    plt.xlim(1,10**6)
    plt.ylim(10**-10,1)
    plt.title("Femto. OC Cap. 1s.", fontweight='bold')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude (V)')
    plt.semilogy()
    plt.semilogx()
    plt.show()
    
    
#==============================================================================
#     # Plot the calculated phase shift for each component frequency
#     plt.plot(xf[yf_amp>Peak_tolerance],yf_phase[yf_amp>Peak_tolerance],'o')
#     #plt.xlim(Min_freq,Max_freq)
#     plt.title("Phase shift of component frequencies", fontweight='bold')
#     plt.xlabel('Frequency (Hz)')
#     plt.ylabel('Phase shift (degrees)')
#     plt.semilogx()
#     plt.show()
#==============================================================================
    
#==============================================================================
#     print 'Peak amplitudes freqs:'
#     print np.transpose(xf[np.logical_and(yf_amp>Peak_tolerance, xf>(Min_freq-10))])
#     print 'Peak amplitudes:'
#     print np.transpose(yf_amp[np.logical_and(yf_amp>Peak_tolerance, xf>(Min_freq-10))])
#     print 'Peak phases:'
#     print np.transpose(yf_phase[np.logical_and(yf_amp>Peak_tolerance, xf>(Min_freq-10))])
#==============================================================================
     
        
#==============================================================================
#aaa = np.arange(2,10)
#print(aaa)
# print(aaa[0:5])
# print(np.mean(aaa[5:10]))
# print(aaa.shape[0]//5)
# print(Bin_Data(aaa,4))
#==============================================================================
