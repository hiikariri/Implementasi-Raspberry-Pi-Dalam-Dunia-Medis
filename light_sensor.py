# import library yang dibutuhkan
import RPi.GPIO as GPIO
import smbus2 as smbus
import time

 # Inisialisasi bus I2C berdasarkan revisi Raspberry Pi
if(GPIO.RPI_REVISION == 1):
    bus = smbus.SMBus(0)
else:
    bus = smbus.SMBus(1)

class LightSensor():

    def __init__(self):

        # Definisikan beberapa variabel berdasarkan datasheet
        self.DEVICE = 0x5c # Alamat default I2C
        self.POWER_DOWN = 0x00 # Status tidak aktif
        self.POWER_ON = 0x01 # Power on
        self.RESET = 0x07 # Reset data nilai register

        # Mulai pengukuran diresolusi 4lx. Waktu biasanya 16ms.
        self.CONTINUOUS_LOW_RES_MODE = 0x13
        # Mulai pengukuran diresolusi 1lx. Waktu biasanya 120ms.
        self.CONTINUOUS_HIGH_RES_MODE_1 = 0x10
        # Mulai pengukuran diresolusi 0.5lx. Waktu biasanya 120ms.
        self.CONTINUOUS_HIGH_RES_MODE_2 = 0x11
        # Mulai pengukuran diresolusi 1lx. Waktu biasanya 120ms.
        # Perangkat secara otomatis diset ke Power Down setelah pengukuran.
        self.ONE_TIME_HIGH_RES_MODE_1 = 0x20
        # Mulai pengukuran diresolusi 0.5lx. Waktu biasanya 120ms.
        # Perangkat secara otomatis diset ke Power Down setelah pengukuran.
        self.ONE_TIME_HIGH_RES_MODE_2 = 0x21
        # Mulai pengukuran diresolusi 1lx. Waktu biasanya 120ms.
        # Perangkat secara otomatis diset ke Power Down setelah pengukuran.
        self.ONE_TIME_LOW_RES_MODE = 0x23

    def convertToNumber(self, data):
        # fungsi sederhana untuk konversi 2 byte data ke bilangan desimal
        return ((data[1] + (256 * data[0])) / 1.2)

    def readLight(self):

        data = bus.read_i2c_block_data(self.DEVICE,self.ONE_TIME_HIGH_RES_MODE_1,16)
        return self.convertToNumber(data)

def main():
    sensor = LightSensor()
    try:
        while True:
            print("Light Level : " + str(sensor.readLight()) + " lx")
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
