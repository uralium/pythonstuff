import keyboard
import time
import webbrowser

bettercalldimi = 'https://i.imgur.com/SDT3tv4.mp4'

print('If you want to call Dimi, press d')
while True:
    try:
        comb = keyboard.is_pressed('d')
        if comb:
            call = print('Ring Ring! Calling Dimi...')
            time.sleep(3)
            webbrowser.open(bettercalldimi)
            break
    except KeyboardInterrupt: # ctrl+c to stop
            print('Hmm looks like Dimi is feeding Stella again ¯\_(ツ)_/¯. Try again later.')
            break