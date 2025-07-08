import RPi.GPIO as GPIO
import time
 
# Mendefinisikan pin motor getaran ke GPIO27
vibration_pin = 27
 
# Mengatur mode GPIO ke GPIO.BCM
GPIO.setmode(GPIO.BCM)
 
# Mengatur pin motor menjadi output
GPIO.setup(vibration_pin, GPIO.OUT)
 
# Menyalakan motor getaran
GPIO.output(vibration_pin, GPIO.HIGH)
# Menunggu selama 0.5 detik
time.sleep(0.5)
# Mematikan motor getaran
GPIO.output(vibration_pin, GPIO.LOW)
# Membersihkan dan mereset GPIO
GPIO.cleanup()
