# Hey Dear Programmer, 
# When I coded this only me and God knew what anything did.
# Now only God knows...
# So if you try to fix the code and failed please add the wasted hours below.

# Total wasted hours: 8

import keyboard
import time
import requests
import html
import re

def main():
    word_list = []
    word_list.append('')
    index = 0
    f = open('./kl.txt', 'a')
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
            word = word_list[-1]
            word_list.append('')
            f.write(word_list[index] + ' ')
            index += 1
            r = requests.get('https://www.thesaurus.com/browse/' + word)
            result = re.findall('(?<=data-linkid="nn1ov4" class="css-1(n6g4vv|kg1yv8|gyuw4i) eh475bn0">)(.*?)(?=<)', r.text)
            print(word)
            print('synonyms:')
            for s in result:
                print(s[1])
            print()
        else:
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == 'backspace':
                    word_list[index] = word_list[index][:-1]
                elif len(event.name) == 1:
                    word_list[index] = word_list[index] + event.name
                
        
    f.close()

if __name__ == '__main__':
    while True:
        main()