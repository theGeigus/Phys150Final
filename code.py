from adafruit_circuitplayground import cp
import time
import math
import random
from analogio import AnalogOut
from analogio import AnalogIn
import board

count = 0
volt = 0
analog_in = AnalogIn(board.A1)
analog_out = AnalogOut(board.A0)

cutoffAccel = 10

while True:
    g = 9.8
    cp.pixels.brightness = 0.05
    x, y, z = cp.acceleration
    a = math.sqrt(x * x + y * y + z * z) / g

    if count == 0:
        t = time.monotonic() - time.monotonic()

    print(a, cutoffAccel)

    if t < 2:
        cp.pixels.fill((255, 75, 0))

    if a > cutoffAccel and volt < 2:
        cp.pixels.fill((255, 255, 255))
        if a > 1.5:
            cp.pixels[1] = (255, 0, 0)
            cp.pixels[2] = (255, 75, 0)
            cp.pixels[3] = (255, 255, 0)
            cp.pixels[4] = (255, 0, 0)
            cp.pixels[5] = (255, 75, 0)
            cp.pixels[6] = (255, 255, 0)
            cp.pixels[7] = (255, 0, 0)
            cp.pixels[8] = (255, 75, 0)
            cp.pixels[9] = (255, 255, 0)
            cp.pixels[0] = (255, 255, 0)
            volt += 1
            print("boom")
            time.sleep(0.1)
    if volt == 1:
        analog_out.value = 65535
        volt += 1
        print(volt)
        time.sleep(0.5)
    if volt == 2:
        if cp.button_a:
            t = 0
            volt = 0
        else:
            cp.pixels.fill((0, 0, 0))
    if t > 120:
        break
    t += .1
    count += 1

    r = random.randint(0, 9) / 100
    cutoffAccel -= r if (cutoffAccel >= 1.5) else 0

    print(t)
    time.sleep(.05)

