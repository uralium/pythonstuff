import pynput
import time


from pynput.keyboard import Key, Controller

keyboard = Controller()

from random import randint
from time import sleep


if __name__ == "__main__":
    while (True):
        with keyboard.pressed(Key.shift):
            sleep(randint(1, 3))
        sleep(randint(1, 3))