import time
import board
import neopixel
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

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

def wheel(pos):
    pos = pos % 256
    if pos < 85:
        return (int(pos * 3), int(255 - pos * 3), 0) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (int(pos * 3), int(255 - pos * 3), 0, 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - pos * 3), 0, int(pos * 3)) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (int(255 - pos * 3), 0, int(pos * 3), 0)
    else:
        pos -= 170
        return (0, int(pos * 3), int(255 - pos * 3)) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (0, int(pos * 3), int(255 - pos * 3), 0)

def rainbow_cycle(wait):
    for j in range(256):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index)
        pixels.show()
        time.sleep(wait)
    pixels.fill((255, 0, 0))
    pixels.show()

def set_pixels(color):
    pixels.fill(color)
    pixels.show()
    time.sleep(0.4)

while True:
    if not bathroom1.value and not bathroom2.value:
        set_pixels((250, 0, 0))
    elif not bathroom1.value or not bathroom2.value:
        for x in range(250, 100, -10):
            set_pixels((x, x//2, 0))
        for x in range(100, 250, 10):
            set_pixels((x, x//2, 0))
    else:
        set_pixels((0, 250, 0))
