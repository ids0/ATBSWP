import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s ')
thelist = ['no', 'test1', 'test2']
i=3
if 'test%s' % (str(i)) in thelist:
    thelist.remove('test%s' % (str(i)))
eggs = 'Hello world!'
bacon = 'HELLO wOrLd!'
print(eggs.lower() == bacon.lower())
assert eggs.lower() == bacon.lower(), 'Eggs and bacon are the same thing?'
assert False, 'dude'
input()



logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')