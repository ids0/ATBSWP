import random
number = int(random.randint(1,20))
numberOfguesses = 5

print('I am thinking of a number between 1 and 20')
for i in range(numberOfguesses):
    print('Take a guess')
    guess = int(input())
    if (guess == number):
        print('Congrats! you guessed the number')
        break
    elif (guess > number):
        print('Too high')
    elif (guess < number):
        print('Too low')
    else:
        print('How?')
input()