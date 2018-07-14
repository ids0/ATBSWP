import threading
import time
print('enter your name')
LOL = input()
print('ok')
print('test of %s' % LOL)

def test():
    time.sleep(2)
    print('yo')

for i in range(0, 5):
    Thread = threading.Thread(target=test)
    Thread.start()
input()
Thread.join()
print('Done.')
