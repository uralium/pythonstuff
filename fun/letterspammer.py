import pynput
import time

from pynput.keyboard import Key, Controller


keyboard = Controller()

try:
    while(True):
        time.sleep(0.1)
        keyboard.type('lol')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    
except KeyboardInterrupt:
    print('Exiting...')
    pass