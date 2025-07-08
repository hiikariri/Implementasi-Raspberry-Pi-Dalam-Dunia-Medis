import RPi.GPIO as GPIO
import time

# Mengatur konfigurasi pin untuk button dan buzzer
button_pin = 26
buzzer_pin = 18

# Mengatur mode GPIO menjadi GPIO.BCM
GPIO.setmode(GPIO.BCM)

# Mengatur pin button sebagai input dengan konfigurasi pull-up resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Mengatur pin buzzer sebagai output
GPIO.setup(buzzer_pin, GPIO.OUT)
try:
    while True:
        # Mengecek jika tombol/button ditekan
        if(GPIO.input(button_pin) == 0):
            # Jika button ditekan, maka pin buzzer diaktifkan
            GPIO.output(buzzer_pin, GPIO.HIGH)
        else:
            # Jika button tidak ditekan, maka pin buzzer dimatikan
            GPIO.output(buzzer_pin, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
