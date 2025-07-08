# import semua library yang dibutuhkan
import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# Buat SPI bus (untuk menginisialisasi protokol SPI pada Raspberry Pi)
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# Buat CS (Chipselect) (memilih tipe SPI yang digunakan. Contoh SPI 0 (pin 24 / gpio 9)) 
cs = digitalio.DigitalInOut(board.CE0)

# Buat objek MCP  
mcp = MCP.MCP3008(spi, cs)

# Buat variabel untuk channel input (contoh dengan CH0 pada MCP3008)  
chan = AnalogIn(mcp, MCP.P0)

# Cetak output  
while True:
    print('Raw ADC Value: ', chan.value)
    print('ADC Voltage: ' + str(chan.voltage) + 'V')
    time.sleep(2)
