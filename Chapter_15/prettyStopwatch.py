#! python3
# prettyStopwatch.py - 

import pprint, datetime, time

print('Press enter to start','Ctrl-C to end',end='')

startTime = time.time()
lastTime = startTime
lap = 1

try:
    while True:
        input()
        lapTime = round(time.time()-lastTime,2)
        totalTime = round(time.time()-startTime,2)
        print(f'Last Lap (total time): {lapTime}({totalTime})',end='')
        lastTime = time.time()
        
except:
    print('Done')



