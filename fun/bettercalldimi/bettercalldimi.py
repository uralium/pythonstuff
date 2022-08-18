import keyboard
import time
import webbrowser

bettercalldimi = 'https://i.imgur.com/SacLumd.mp4'
roll = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'

print('If you want to call Dimi, press d')
print('Or rather, what if you press r first?')
while True:
    try:
        comb = keyboard.is_pressed('d')
        comb2 = keyboard.is_pressed('r')
        if comb:
            print('Ring Ring! Calling Dimi...')
            time.sleep(3)
            webbrowser.open(bettercalldimi)
            print('What about r?')
        elif comb2:
            print("lmao n00b you're in for a ride!!1")
            time.sleep(3)
            webbrowser.open(roll)
            break
    except KeyboardInterrupt: # ctrl+c to stop
            print('Hmm looks like Dimi is feeding Stella again ¯\_(ツ)_/¯. Try again later.')
            break