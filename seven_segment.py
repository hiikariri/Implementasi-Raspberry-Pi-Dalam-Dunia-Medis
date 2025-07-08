import time
import datetime
from Adafruit_LED_Backpack import SevenSegment
 
# ===========================================================================
# Menampilkan Jam/Waktu
# ===========================================================================
segment = SevenSegment.SevenSegment(address=0x70)
 
# Inisialisasi display
segment.begin()
 
print("Press CTRL+C to exit")
 
# Melakukan update secara terus menerus untuk 4 karakter, 7-segment display
try:
  while(True):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
 
    segment.clear()
    # Set jam
    segment.set_digit(0, int(hour / 10))     # Puluhan
    segment.set_digit(1, hour % 10)          # Satuan
    # Set menit
    segment.set_digit(2, int(minute / 10))   # Puluhan
    segment.set_digit(3, minute % 10)        # Satuan
    # menyalakan titik dua/colon (:)
    segment.set_colon(second % 2)              # Menyalakan colon pada 1Hz
 
    # Write buffer display ke hardware untuk mengupdate display secara fisikal
    segment.write_display()
 
    # Menunggu selama 0.25 detik 
    time.sleep(0.25)
except KeyboardInterrupt:
    segment.clear()
    segment.write_display()
