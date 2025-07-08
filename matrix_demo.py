import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

def main(cascaded, block_orientation, rotate):
    # inisialisasi dan deklarasi perangkat matrix demo
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=cascaded or 1, block_orientation=block_orientation, rotate=rotate or 0)
    # untuk proses debugging
    print("[-] Matrix initialized")

    # cetak hello world pada matrix demo
    msg = "Hello World"
    # untuk proses debugging
    print("[-] Printing: %s" % msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)


if __name__ == "__main__":
# cascaded = Jumlah dari MAX7219 yang digunakan, defaultnya adalah 1 (jika menggunakan beberapa blok matrix, maka dapat disesuaikan.
# block_orientation = pilihannya 0, 90, -90, digunakan untuk inisialisasi matrix demo untuk mengatur orientasi fisik blok LED saat pertama kali digunakan, defaultnya 0
# rotate = pilihannya 0, 1, 2, 3, untuk rotasi tampilan, dimana 0=0°, 1=90°, 2=180°, 3=270°, default=0
    try:
        main(cascaded=1, block_orientation=90, rotate=0)
    except KeyboardInterrupt:
        pass
