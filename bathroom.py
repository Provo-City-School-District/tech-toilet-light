import time
import board
import neopixel
from time import sleep
import digitalio

bathroom1 = digitalio.DigitalInOut(board.D23)
bathroom1.direction = digitalio.Direction.INPUT
bathroom1.pull = digitalio.Pull.UP

bathroom2 = digitalio.DigitalInOut(board.D24)
bathroom2.direction = digitalio.Direction.INPUT
bathroom2.pull = digitalio.Pull.UP

pixel_pin = board.D18

num_pixels = 300

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)

def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
        pixels.fill((255, 0, 0))
        pixels.show()

while True:
    if  bathroom1.value==0 and bathroom2.value==0:
        pixels.fill((250, 0, 0))
        pixels.show()
        time.sleep(0.4)
    elif bathroom1.value==0 or bathroom2.value==0:
        for x in range(75,250,10):
            pixels.fill((x,20,x))
            pixels.show()
            time.sleep(.04)
        for x in range(250,75,-10):
            pixels.fill((x,20,x))
            pixels.show()
            time.sleep(.04)
    else:
        pixels.fill((0, 250, 0))
        pixels.show()
        time.sleep(0.4)
