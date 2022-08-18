from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

def send_range(start, end, wait_time):
    for i in range(start, end+1):
        keyboard.type(str(i))
        keyboard.press(Key.enter)
        time.sleep(wait_time)

send_range(1, 50, 0)