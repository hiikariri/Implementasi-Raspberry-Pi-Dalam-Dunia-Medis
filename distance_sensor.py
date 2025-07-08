import RPi.GPIO as GPIO
import time
 
# Mengatur mode GPIO ke GPIO.BCM
GPIO.setmode(GPIO.BCM)

# Mendefinisikan pin sensor untuk trigger dan echo
TRIG = 16
ECHO = 12
# Mengatur mode pin sensor, trigger sebagai output dan echo sebagai input
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN) 

# Inisialisasi untuk mereset sensor
GPIO.output(TRIG, False)                                                      
print("Waiting For Sensor To Settle")                                          
time.sleep(2) 
GPIO.output(TRIG, True)                                                  
time.sleep(0.00001)                                                        
GPIO.output(TRIG, False)

# Melakukan pencatatan waktu deteksi gelombang
while GPIO.input(ECHO)==0:
  pulse_start = time.time()
while GPIO.input(ECHO)==1:
  pulse_end = time.time()

# Menghitung durasi waktu pancar hingga terima gelombang
pulse_duration = pulse_end - pulse_start

# Menghitung jarak dengan mengalikan waktu dengan kecepatan gelombang suara
distance = pulse_duration * 17150
distance = round(distance, 2)
print("Distance: %scm" % distance)
GPIO.cleanup()
