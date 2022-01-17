import pynput
import time

from pynput.keyboard import Key, Controller


keyboard = Controller()

while(True):
    try:
        time.sleep(0.5)
        keyboard.type('Your text here')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        
    except:
        if keyboard.press(Key.enter):
            print('You paused the code!')
            break
            