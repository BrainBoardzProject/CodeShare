"""
Author: Salim Haniff
Email: salimwp@gmail.com
Description: Read analog input from a potentiometer
"""

import time
import board
from analogio import AnalogIn
import math

analog_in = AnalogIn(board.IO3)

def get_value(pin):
    return math.floor((analog_in.value / 52924) * 100)

while True:
    print(get_value(analog_in.value))
    time.sleep(1)