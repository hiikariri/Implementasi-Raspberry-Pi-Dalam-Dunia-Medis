import sys
import Adafruit_DHT
 
# Setup tipe sensor
sensor = 11
# Set pin sensor
pin = 4

# Membaca nilai kelembapan dan temperatur
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
