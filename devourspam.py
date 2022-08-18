import pynput
import time

from pynput.keyboard import Key, Controller


keyboard = Controller()

try:
    while(True):
        time.sleep(0.1)
        keyboard.press(Key.one)
        keyboard.release(Key.one)
    
except KeyboardInterrupt:
    pass