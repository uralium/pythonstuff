#Execute the script, then highlight something. It will turn the 
#highlighted text into sponge-text and put it in your clip board.
#Noice

import random
import pyautogui as pya #Used to press ctrl-c
import pyperclip #Handy cross-platform clipboard text handler
import time

time.sleep(5) #Gives a 5 second delay, so you can highlight stuff

def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01) #ctrl-c is usually very fast but the program may execute faster
    return pyperclip.paste()

text = str(copy_clipboard()) #This copies what you have highlighted and makes it to a string

def capi_sentence(sentence): #The sentence-converter starts here
    new_sentence = ""
    number = 0 #Dummy number for tracki

    for letter in sentence.lower():
        if len(new_sentence)<2: #Creates the first two letter
            random_number = random.randint(0,1) #This randomly decides if the letter should be upper or lowercase
            if random_number==0:
                new_sentence += letter.upper()
            else:
                new_sentence += letter
        else:
            if (new_sentence[number-2].isupper() and new_sentence[number-1].isupper() or new_sentence[number-2].islower() and new_sentence[number-1].islower())==True:
                #Checks if the two letters before are both upper or lowercase
                if new_sentence[number-1].isupper(): #Makes the next letter the opposite of the letter before
                    new_sentence += letter.lower()
                else:
                    new_sentence += letter.upper()
            else:
                random_number = random.randint(0,1)
                if random_number==0:
                    new_sentence += letter.upper()
                else:
                    new_sentence += letter
                
        number += 1 #Add one more to the tracking
     
    pyperclip.copy(str(new_sentence)) #Copies the new sentence as a string to the clip board
    
capi_sentence(text) #The executioner
