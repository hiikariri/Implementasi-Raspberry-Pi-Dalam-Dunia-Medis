#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt

# Modify the library path of High-Pricision_AD_HAT library!
sys.path.append('/home/<user>/High-Pricision_AD_HAT/python')
import ADS1263

# Constants
REF = 2.5  # Modify according to actual voltage
           # external AVDD and AVSS(Default), or internal 2.5V
sampling_freq = 1200  # Sampling frequency (same as data rate used)
sampling_time = 10    # Total sampling time (seconds)
sampling_interval = 1.0 / sampling_freq  # Time period
buffer_size = sampling_freq * sampling_time  # Buffer size for the data
time_buffer = np.arange(0, sampling_time, sampling_interval)
ecg_buffer = []  # Circular buffer for ECG data

# Initialize ADC ADS1263
try:
    ADC = ADS1263.ADS1263()
    if (ADC.ADS1263_init_ADC1('ADS1263_1200SPS') == -1):  # data rate
        exit()
    ADC.ADS1263_SetMode(0)  # 0 is singleChannel, 1 is diffChannel
    channel = 0  # The channel must be less than 10
    
    def get_ecg_value():
        """ Reads ECG value from ADS1263 """
        # Read the channel value
        ADC_Value = ADC.ADS1263_GetChannalValue(channel)
        if(ADC_Value >> 31 == 1):
            ecg_value = (REF * 2 - ADC_Value * REF / 0x80000000)  
        else:
            ecg_value = (ADC_Value * REF / 0x7fffffff) # 32 bit
        return ecg_value 
    
    while (len(ecg_buffer) < buffer_size):
        ecg_buffer.append(get_ecg_value())
        
    # Setup plot
    fig, ax = plt.subplots()
    line, = ax.plot(time_buffer, ecg_buffer, 'r')
    
    # Set plot limits
    ax.set_ylim(-REF, REF)
    ax.set_xlim(time_buffer[0], time_buffer[-1])
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude (mV)')
    ax.set_title('ECG Signal')
    
    plt.show()
    ADC.ADS1263_Exit()

except IOError as e:
    print(e)
   
except KeyboardInterrupt:
    print("ctrl + c:")
    print("Program end")
    ADC.ADS1263_Exit()
    exit()
