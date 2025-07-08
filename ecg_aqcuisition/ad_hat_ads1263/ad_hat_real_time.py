#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import time
import threading
import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# Modify the library path of High-Pricision_AD_HAT library!
sys.path.append('/home/<user>/High-Pricision_AD_HAT/python')
import ADS1263

# Constants
REF = 2.5   # Modify according to actual voltage
            # external AVDD and AVSS(Default), or internal 2.5V
sampling_freq = 1200  # Sampling frequency 
sampling_interval = 1.0 / sampling_freq  # Time period
buffer_size = sampling_freq * 2  # Buffer size for 2 seconds of data
time_buffer = deque(np.linspace(-2, 0, buffer_size), maxlen=buffer_size)
ecg_buffer = deque(np.zeros(buffer_size), maxlen=buffer_size) # Buffer
running = True

# Initialize ADC ADS1263
try:
    ADC = ADS1263.ADS1263()
    # ADC configuration
    if (ADC.ADS1263_init_ADC1('ADS1263_1200SPS') == -1):
        exit()
    ADC.ADS1263_SetMode(0)  # 0 is singleChannel, 1 is diffChannel
    channel = 0  # The channel must be less than 10
    
    def get_ecg_value():
        """ Reads ECG value from ADS1263 """
        ADC_Value = ADC.ADS1263_GetChannalValue(channel) # Read value
        if(ADC_Value >> 31 == 1):
            ecg_value = (REF * 2 - ADC_Value * REF / 0x80000000)  
        else:
            ecg_value = (ADC_Value * REF / 0x7fffffff) # 32 bit
        return ecg_value
            
    def data_aquisition():
        """ Data aquisition in different thread """
        global running
        next_sample_time = time.time()
        
        while running:
            ecg_value = get_ecg_value()
            
            ecg_buffer.append(ecg_value)
            time_buffer.append(time_buffer[-1] + sampling_interval)
      
            # Sleep to maintain sampling rate
            next_sample_time += sampling_interval
            sleep_time = next_sample_time - time.time() 
            if sleep_time > 0:
                time.sleep(sleep_time)
    
    data_thread = threading.Thread(target=data_aquisition, daemon=True)
    data_thread.start()
    
    # Setup real-time plot
    fig, ax = plt.subplots()
    line, = ax.plot(time_buffer, ecg_buffer, 'r')
    
    # Set plot limits
    ax.set_ylim(-REF, REF)
    ax.set_xlim(time_buffer[0], time_buffer[-1])
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude (mV)')
    ax.set_title('ECG Signal')
    
    def update(frame):
        line.set_ydata(ecg_buffer)
        line.set_xdata(time_buffer)
        ax.set_xlim(time_buffer[0], time_buffer[-1])
        return line,
    
    # Start real-time animation
    using_blit = True   # Set blit True for faster faster performance,
                        # but this will not update the figure (time axis)
    if using_blit:
        ax.set_xticks([])
        ax.set_xticklabels([])
        
    ani = animation.FuncAnimation(fig, update, interval=15, blit=using_blit) 
    plt.show()
    
    running = False
    data_thread.join()
    ADC.ADS1263_Exit()

except IOError as e:
    print(e)
   
except KeyboardInterrupt:
    print("ctrl + c:")
    print("Program end")
    ADC.ADS1263_Exit()
    exit()
