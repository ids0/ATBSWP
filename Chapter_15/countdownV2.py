#! python3
# countdownV2.py - A simple countdown script
import time, subprocess

timeToWait = 60

for i in range(timeToWait):
    time.sleep(1)
    print(f'Time remaining:{(timeToWait-i):02}')
subprocess.Popen(['start',r'D:\Drive\Code\ATBSWP\Chapter_15\alarm.wav'], shell=True)
