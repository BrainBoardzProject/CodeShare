"""
Author: Salim Haniff
Email: salimwp@gmail.com
Description: Simple code to blink the LED
"""

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)