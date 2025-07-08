import RPi.GPIO as GPIO
import time

# Mendefinisikan pin touch sensor pada GPIO17
touch_pin = 17

# Mengatur mode GPIO ke GPIO.BCM
GPIO.setmode(GPIO.BCM)
 
# Mengatur pin touch sensor menjadi input dengan konfigurasi pull-down resistor
GPIO.setup(touch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
try:
    while True:
        # Mengecek status touch sensor
        if(GPIO.input(touch_pin)):
            print('Touch Detected') # Jika ada sentuhan, print ke terminal
        time.sleep(0.1)
except KeyboardInterrupt:
    # CTRL+C terdeteksi, membersihkan dan menghentikan program
    GPIO.cleanup()
