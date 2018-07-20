#! python3
# countdown.py - A simple countdown script.

import time, subprocess,os

timeLeft = 1
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft = timeLeft - 1 

# # At the end of the countdown, play a sound file.
# subprocess.Popen(['start',r'D:\Drive\Code\ATBSWP\Chapter_15\alarm.wav'], shell=True)

magnet = "magnet:?xt=urn:btih:27628b48b09f96e46a124c62fdc81c49fe54dbdf&dn=Sharp.Objects.S01E01.1080p.WEBRip.6CH.x265.HEVC-PSA&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Fzer0day.ch%3A1337&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969"
# subprocess.Popen(['start',magnet], shell=True)
os.startfile(magnet)