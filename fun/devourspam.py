import pyautogui
import time

while True:
    try:
        for i in range(5):
            time.sleep(1)
            pyautogui.press("1")
            time.sleep(1)
            pyautogui.press("2")
            time.sleep(1)
            pyautogui.press("3")
            time.sleep(1)
            pyautogui.press("4")
            time.sleep(1)


    except KeyboardInterrupt:
        print('Exiting...')
        break