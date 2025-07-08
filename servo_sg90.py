import RPi.GPIO as GPIO
import time
import sys

class sg90:

  def __init__( self, direction):
    # Inisialisasi servo pada pin 25 dengan mode BCM
    self.pin = 25
    GPIO.setmode( GPIO.BCM )
    GPIO.setup( self.pin, GPIO.OUT )
    self.direction = int( direction )
    self.servo = GPIO.PWM( self.pin, 50 )  # Inisialisasi PWM dengan frekuensi 50Hz
    self.servo.start(0.0)  # Mulai PWM dengan duty cycle 0

  def cleanup( self ):
    # Menghentikan servo dengan mengatur duty cycle ke posisi netral
    self.servo.ChangeDutyCycle(self._henkan(0))
    time.sleep(0.3)
    self.servo.stop()
    GPIO.cleanup()  

  def currentdirection( self ):
    # Mengembalikan arah saat ini dari servo
    return self.direction

  def _henkan( self, value ):
    # Konversi nilai arah ke duty cycle untuk servo
    return 0.05 * value + 7.0

  def setdirection( self, direction, speed ):
    # Menggerakkan servo dari posisi saat ini ke arah tujuan dengan kecepatan tertentu
    for d in range( self.direction, direction, int(speed) ):
      self.servo.ChangeDutyCycle( self._henkan( d ) )
      self.direction = d
      time.sleep(0.1)  # Beri jeda untuk pergerakan servo
    self.servo.ChangeDutyCycle( self._henkan( direction ) )  # Pastikan posisi akhir akurat
    self.direction = direction

def main():
    # Fungsi utama untuk menjalankan servo secara terus-menerus
    s = sg90(0)  # Inisialisasi servo dengan arah awal 0

    try:
        while True:
            print("Turn left ...")
            s.setdirection( 100, 80 )  # Putar ke kiri
            time.sleep(0.5)
            print("Turn right ...")
            s.setdirection( -100, 80 )  # Putar ke kanan
            time.sleep(0.5)
    except KeyboardInterrupt:
        s.cleanup()  # Bersihkan GPIO saat program dihentikan

if __name__ == "__main__":
    main()
GPIO.cleanup()
