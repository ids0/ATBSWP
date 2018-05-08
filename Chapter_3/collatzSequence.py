def collatz(number):
    if (number % 2 == 0):
        print(number// 2)
        return(number // 2)
    else:
        print(3*number + 1)
        return(3*number + 1)

def collatzSequence(input):
    try:
        n = int(input)
        ((n+1) // n)
    except:
        print('Not a valid input, please enter a number')
        return
    while True:
        if n != 1:
            n = collatz(n)
            continue
        else:
            break
print('Enter number:')
firstNumber= input()
collatzSequence(firstNumber)
input()