import keyboard
import time
import webbrowser

bettercalldimi = 'https://i.imgur.com/SacLumd.mp4'
bettercallchinesedimi = 'https://i.imgur.com/6a6jrvy.mp4'
roll = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'

print('If you want to call Dimi, press d')
print('If you want to call Chinese Dimi, press c')
print('Or rather, what if you press r first?')
while True:
    try:
        comb = keyboard.is_pressed('d')
        comb2 = keyboard.is_pressed('r')
        comb3 = keyboard.is_pressed('c')
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
        elif comb3:
            print("環環！打電話給迪米...")
            time.sleep(3)
            webbrowser.open(bettercallchinesedimi)
            break
    except KeyboardInterrupt: # ctrl+c to stop
            print('Hmm looks like Dimi is feeding Stella again ¯\_(ツ)_/¯. Try again later.')
            break