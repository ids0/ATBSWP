import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coint toss! Ender heads or tails:')
    guess = input()
toss = random.randint(0,1) # 0 is tails, 1 is heads
if toss == 0:
    toss = 'tails'
else:
    toss = 'heads'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    while guess not in ('heads', 'tails'):
        print('Nope! Guess again!')
        guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
