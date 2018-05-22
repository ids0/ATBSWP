import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def facotial(n):
    logging.debug('Start of facotial(%s%%)' % (n))
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of facotial (%s%%)' % (n))
    return total

print(facotial(5))
logging.debug('End of program')