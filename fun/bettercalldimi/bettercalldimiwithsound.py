import keyboard
import time
import webbrowser
from playsound import playsound

bettercalldimi = 'https://i.imgur.com/SacLumd.mp4'

print('If you want to call Dimi, press d')
while True:
    try:
        comb = keyboard.is_pressed('d')
        if comb:
            print('Ring Ring! Calling Dimi...')
            playsound('bettercalldimi/assets/note.mp3')
            time.sleep(3)
            webbrowser.open(bettercalldimi)
            break
    except KeyboardInterrupt: # ctrl+c to stop
            print('Hmm looks like Dimi is feeding Stella again ¯\_(ツ)_/¯. Try again later.')
            break