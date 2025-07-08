import RPi.GPIO as GPIO
import time
# Mendefinisikan pin relay pada GPIO21
relay_pin = 21
# Mengatur mode GPIO menjadi GPIO.BCM dan mengatur pin relay sebagai output
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

# Membuka relay
GPIO.output(relay_pin, GPIO.LOW)
time.sleep(0.5)
# Menutup relay
GPIO.output(relay_pin, GPIO.HIGH)
time.sleep(0.5)
# Membuka relay
GPIO.output(relay_pin, GPIO.LOW)

GPIO.cleanup()
