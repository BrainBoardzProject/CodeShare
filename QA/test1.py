"""
Author: Salim Haniff
Email: salimwp@gmail.com
Description: Basic QA test 1
"""

import time
import board
import busio
import array
import audiobusio
import audiocore
import digitalio

uart = busio.UART(board.IO43, board.IO44, baudrate=9600)
led = digitalio.DigitalInOut(board.IO42)
led.direction = digitalio.Direction.OUTPUT
a = audiobusio.I2SOut(board.IO45, board.IO35, board.IO41)

while True:
    uart.write(bytearray(b'Hello from UART'))
    print("Hello from USB")
    led.value = True
    time.sleep(2)
    led.value = False
    time.sleep(2)