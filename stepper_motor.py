# import library yang dibutuhkan
import RPi.GPIO as GPIO
import math
import time

 # Kelas untuk stepmotor
class Stepmotor:
	def __init__(self):
		# Atur mode GPIO
		GPIO.setmode(GPIO.BCM)
		# Deklarasikan pin yang digunakan pada Raspberry Pi
		self.pin_A = 5
		self.pin_B = 6
		self.pin_C = 13
		self.pin_D = 19
		self.interval = 0.010

		# Deklarasikan pin yang digunakan sebagai output

		GPIO.setup(self.pin_A,GPIO.OUT)
		GPIO.setup(self.pin_B,GPIO.OUT)
		GPIO.setup(self.pin_C,GPIO.OUT)
		GPIO.setup(self.pin_D,GPIO.OUT)
             # Kondisi awal setiap output adalah false (motor tidak bergerak)
		GPIO.output(self.pin_A, False)
		GPIO.output(self.pin_B, False)
		GPIO.output(self.pin_C, False)
		GPIO.output(self.pin_D, False)

    # Kondisi setiap output untuk pergerakan motor
	def Step1(self):
		GPIO.output(self.pin_D, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_D, False)

	def Step2(self):
		GPIO.output(self.pin_D, True)
		GPIO.output(self.pin_C, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_D, False)
		GPIO.output(self.pin_C, False)

	def Step3(self):
		GPIO.output(self.pin_C, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_C, False)

	def Step4(self):
		GPIO.output(self.pin_B, True)
		GPIO.output(self.pin_C, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_B, False)
		GPIO.output(self.pin_C, False)

	def Step5(self):
		GPIO.output(self.pin_B, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_B, False)

	def Step6(self):
		GPIO.output(self.pin_A, True)
		GPIO.output(self.pin_B, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_A, False)
		GPIO.output(self.pin_B, False)

	def Step7(self):
		GPIO.output(self.pin_A, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_A, False)

	def Step8(self):
		GPIO.output(self.pin_D, True)
		GPIO.output(self.pin_A, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_D, False)
		GPIO.output(self.pin_A, False)
   
   # fungsi pergerakan motoor
	def turn(self,count):
		for i in range (int(count)):
			self.Step1()
			self.Step2()
			self.Step3()
			self.Step4()
			self.Step5()
			self.Step6()
			self.Step7()
			self.Step8()
   # fungsi akhir (selesai/tutup)
	def close(self):
		# Bersihkan penggunaan GPIO
		GPIO.cleanup()
   # fungsi pergerakan motor sebanyak n langkah
	def turnSteps(self, count):
		# motor akan bergerak sebanyak n langkah (sesuai input yang diberikan)
		for i in range (count):
			self.turn(1)
   # fungsi pergerakan motor sebanyak n derajat
	def turnDegrees(self, count):
		# pergerakan motor sejauh n derajat (berdasarkan input)
		self.turn(round(count*512/360,0))

   # fungsi pergerakan motor sejauh jarak n
	def turnDistance(self, dist, rad):
		# pergerakan motor berdasarkan jarak yang diinputkan
		self.turn(round(512*dist/(2*math.pi*rad),0))
# fungsi utama
def main():
	print("moving started")
	motor = Stepmotor()
	print("One Step")
	motor.turnSteps(1)
	time.sleep(0.5)
	print("20 Steps")
	motor.turnSteps(20)
	time.sleep(0.5)
	print("quarter turn")
	motor.turnDegrees(90)
	print("moving stopped")
	motor.close()

if __name__ == "__main__":
    main()
