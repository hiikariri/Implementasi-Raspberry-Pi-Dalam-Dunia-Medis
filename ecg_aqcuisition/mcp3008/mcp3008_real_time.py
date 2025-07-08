import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import threading
 
sampling_freq = 1200;
sampling_interval = 1.0/sampling_freq
buffer_size = sampling_freq*2
time_buffer = deque(np.linspace(-2, 0, buffer_size), maxlen=buffer_size)
ecg_buffer = deque(np.zeros(buffer_size), maxlen=buffer_size)
running = True

spi = busio.SPI(clock = board.SCK, MISO = board.MISO, MOSI = board.MOSI)
cs = digitalio.DigitalInOut(board.CE0) 
mcp = MCP.MCP3008(spi, cs)
chan = AnalogIn(mcp, MCP.P1)

try:
    def get_ecg_value():
       ecg_value = chan.voltage
       return ecg_value
 
    def data_aquisition():
       global running
       next_sample_time = time.time()
    
       while running :
           ecg_value = get_ecg_value()
        
           ecg_buffer.append(ecg_value)
           time_buffer.append(time_buffer[-1] + sampling_interval)
        
           next_sample_time+=sampling_interval
           sleep_time = next_sample_time-time.time()
           if sleep_time>0:
               time.sleep(sleep_time)
 
    data_thread = threading.Thread(target=data_aquisition, daemon=True)
    data_thread.start()
    
    fig, ax = plt.subplots()
    line, = ax.plot(time_buffer, ecg_buffer, 'r')
    
    ax.set_ylim(-3,3)
    ax.set_xlim(time_buffer[0], time_buffer[-1])
    ax.set_ylabel('Amplutide (mV)')
    ax.set_xlabel('time (s)')
    ax.set_title('ECG Signal')
    
    def update(frame):
        line.set_ydata(ecg_buffer)
        line.set_xdata(time_buffer)
        ax.set_xlim(time_buffer[0], time_buffer[-1])
        return line,
    
    using_blit = True
    if using_blit :
        ax.set_xticks([])
        ax.set_xticklabels([])
        
    ani = animation.FuncAnimation(fig, update, interval=15, blit=using_blit)
    plt.show()
    running = False
    data_thread.join()
 
except KeyboardInterrupt :
    print("ctrl + c")
    print("program end")
    exit()
