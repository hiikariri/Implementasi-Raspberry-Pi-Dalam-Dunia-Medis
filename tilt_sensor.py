import time
import RPi.GPIO as GPIO
 
# Mendefinisikan pin sensor tilt
tilt_pin = 23
 
# Mengatur mode GPIO ke GPIO.BCM
GPIO.setmode(GPIO.BCM)
# Mengatur pin sensor tilt sebagai input
GPIO.setup(tilt_pin, GPIO.IN)
 
try:
    while True:
        # nilai pembacaan positif jika miring ke kiri,
        # negatif jika miring ke kanan
        if GPIO.input(tilt_pin):
            print("[-] Left Tilt")
        else:
            print("[-] Right Tilt")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
