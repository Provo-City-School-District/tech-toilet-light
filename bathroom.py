pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

def wheel(pos):
    pos = pos % 256  # Ensure pos is within 0-255
    if pos < 85:
        return (int(pos * 3), int(255 - pos * 3), 0) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (int(pos * 3), int(255 - pos * 3), 0, 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - pos * 3), 0, int(pos * 3)) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (int(255 - pos * 3), 0, int(pos * 3), 0)
    else:
        pos -= 170
        return (0, int(pos * 3), int(255 - pos * 3)) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (0, int(pos * 3), int(255 - pos * 3), 0)

def rainbow_cycle(wait):
    for j in range(256):  # Increased range to 256 for smoother color transition
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index)
        pixels.show()
        time.sleep(wait)

def set_pixels(color):
    pixels.fill(color)
    pixels.show()
    time.sleep(0.4)

while True:
    if bathroom1.value == 0 and bathroom2.value == 0:
        set_pixels((250, 0, 0))
    elif bathroom1.value == 0 or bathroom2.value == 0:
        for x in range(75, 250, 10):
            set_pixels((x, 20, x))
        for x in range(250, 75, -10):
            set_pixels((x, 20, x))
    else:
        set_pixels((0, 250, 0))