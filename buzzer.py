import RPi.GPIO as GPIO
import time
# Mendefinisikan pin buzzer pada GPIO18
buzzer_pin = 18
# Mengatur mode GPIO menjadi GPIO.BCM
GPIO.setmode(GPIO.BCM)
# Mengatur mode pin buzzer menjadi output
GPIO.setup(buzzer_pin, GPIO.OUT)

# Mengaktifkan pin buzzer sehingga buzzer mengeluarkan suara
GPIO.output(buzzer_pin, GPIO.HIGH)
# Menunggu selama 0.5 detik
time.sleep(0.5)
# Mematikan pin buzzer
GPIO.output(buzzer_pin, GPIO.LOW)

GPIO.cleanup()
