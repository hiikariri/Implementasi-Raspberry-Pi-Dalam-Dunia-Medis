#!/usr/bin/python
# -*- coding:utf-8 -*-
 
import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
 
# Constants
REF = 2.5  # Modify according to actual voltage
           # external AVDD and AVSS(Default), or internal 2.5V
sampling_freq = 1200  # Sampling frequency (same as data rate used)
sampling_time = 10    # Total sampling time (seconds)
sampling_interval = 1.0 / sampling_freq  # Time period
buffer_size = sampling_freq * sampling_time  # Buffer size for the data
time_buffer = np.arange(0, sampling_time, sampling_interval)
ecg_buffer = []  # buffer for ECG data
 
# Initialize ADC ADS1263
spi = busio.SPI(clock = board.SCK, MISO = board.MISO, MOSI = board.MOSI)
cs = digitalio.DigitalInOut(board.CE0) 
mcp = MCP.MCP3008(spi, cs)
chan = AnalogIn(mcp, MCP.P1)
try:
    def get_ecg_value():
        """ Reads ECG value from MCP3008 """
        ecg_value = chan.voltage
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
 
except IOError as e:
    print(e)
   
except KeyboardInterrupt:
    print("ctrl + c:")
    print("Program end")
    exit()
