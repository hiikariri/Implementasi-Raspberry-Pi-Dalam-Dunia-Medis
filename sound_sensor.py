import RPi.GPIO as GPIO
import time
 
# Mendefinisikan pin sensor suara
sound_pin = 24
 
# Mengatur mode GPIO menjadi GPIO.BCM
GPIO.setmode(GPIO.BCM)
# Mengatur pin sensor sebagai input
GPIO.setup(sound_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
try:
    while True:
       if(GPIO.input(sound_pin)==GPIO.LOW):
             print("suara terdeteksi")
             time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
