from adafruit_circuitplayground import cp
import time
import math
import random

count = 0

while True:
    g = 9.8
    cp.pixels.brightness = 0.05
    x, y, z = cp.acceleration
    a = math.sqrt(x * x + y * y + z * z) / g

    if count == 0:
        t = time.monotonic() - time.monotonic()

    if t > random.randint(10, 20):
        cp.pixels[1] = ((255, 0, 0))
        cp.pixels[2] = ((255, 75, 0))
        cp.pixels[3] = ((255, 255, 0))
        cp.pixels[4] = ((255, 0, 0))
        cp.pixels[5] = ((255, 75, 0))
        cp.pixels[6] = ((255, 255, 0))
        cp.pixels[7] = ((255, 0, 0))
        cp.pixels[8] = ((255, 75, 0))
        cp.pixels[9] = ((255, 255, 0))
        cp.pixels[0] = ((255, 255, 0))
        print("boom")
        time.sleep(900000000000)

    t += 1
    count += 1
    print(t)
    time.sleep(1)
