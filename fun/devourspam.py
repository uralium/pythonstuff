import pyautogui
import time

while True:
    try:
        for i in range(3):
            time.sleep(0.1)
            pyautogui.press("1")

    except KeyboardInterrupt:
        print('Exiting...')
        break