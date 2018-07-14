#! python3
# countdown.py - A simple countdown script.

import time, subprocess

timeLeft = 6
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft = timeLeft - 1 

# At the end of the countdown, play a sound file.
subprocess.Popen(['start',r'D:\Drive\Code\ATBSWP\Chapter_15\alarm.wav'], shell=True)