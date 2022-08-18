import keyboard
import time
import webbrowser

bettercalldimi = 'https://imgur.com/a/3hKNLTl'


print('If you want to call Dimi, press ALT+SHIFT+D')

if keyboard.is_pressed('alt+shift+d'):
    print('Ring Ring! Calling Dimi...')
    time.sleep(5)
    webbrowser.open(bettercalldimi)
else:
    print('Hmm looks like Dimi is feeding Stella again ¯\_(ツ)_/¯')