import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522 
reader = SimpleMFRC522
try:
    text = input("New Data : ")
    print("Letakkan kartu Anda untuk dicatat")
    reader.write(text)
    print("Kode kartu tercatat")

finally:
    GPIO.cleanup()