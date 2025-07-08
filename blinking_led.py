import time
import RPi.GPIO as GPIO
 
# Mendefinisikan pin GPIO LED
led_pin = 26
 
# Mengatur mode GPIO menjadi GPIO.BCM
GPIO.setmode(GPIO.BCM)
# Mengatur pin LED sebagai output
GPIO.setup(led_pin, GPIO.OUT)
 
try:
    while True:
        # Mengaktifkan pin LED
        GPIO.output(led_pin, GPIO.HIGH)
        # Menunggu selama 0.2 detik
        time.sleep(0.2)
        # Mematikan pin LED
        GPIO.output(led_pin, GPIO.LOW)
        # Menunggu selama 0.2 detik
        time.sleep(0.2)
except KeyboardInterrupt:
    # CTRL+C terdeteksi, membersihkan dan menghentikan program
    GPIO.cleanup()
