#! python3
# mouseNowV2.py - 

import pyautogui, traceback, time
x,y = (-1,-1)
print('Ctrl-C to quit')
try:
    while True: 
        if (x,y) != pyautogui.position(): 
            x,y = pyautogui.position()
            print(f'X: {x} Y: {y}')
            time.sleep(1)
except KeyboardInterrupt:
    print('User Interrupted')