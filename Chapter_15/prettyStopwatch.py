#! python3
# prettyStopwatch.py - 

import pprint, datetime, time

print('Press enter to start',end='')
print('Ctrl-C to end',end='')

startTime = time.time()
lastTime = startTime
lap = 1
len1 = 23
len2 = 8
len3 = 9

def printsw(text):
    pass

try:
    while True:
        input()
        lapTime = round(time.time()-lastTime,2)
        totalTime = round(time.time()-startTime,2)
        text1 = f'Lap #{lap:02} (total time):'
        text2 = f' {lapTime} ('
        text3 = f'{totalTime})s'
        toPrint = f'Lap #{lap:02} (total time): {lapTime} ({totalTime})s'
        print(text1.ljust(len1)+text2.center(len2)+text3.ljust(len3),end='')
        lap += 1
        lastTime = time.time()
        
except KeyboardInterrupt:
    print('Done')
    input()


