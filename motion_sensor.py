import RPi.GPIO as GPIO
import time
 
# Mendefinisikan pin sensor gerakan
motion_pin = 23
 
# Mengatur mode GPIO menjadi GPIO.BCM
GPIO.setmode(GPIO.BCM)
# Mengatur mode pin sensor gerakan sebagai input
GPIO.setup(motion_pin, GPIO.IN)
 
try:
    while True:
       if(GPIO.input(motion_pin) == 0):
             print("Nothing moves ...") # Print saat tidak terdeteksi gerakan
       elif(GPIO.input(motion_pin) == 1):
             print("Motion detected!") # Print saat terdeteksi gerakan
       time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
