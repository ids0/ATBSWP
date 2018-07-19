#! python3
# montyHall.py - Monty Hall problem simulator

import random

first = 0
noFirst = 0
n = 1000000
print('Playing the game...')
for game in range(n):

    # Assing numbers to doors
    doors = {}
    number = [1,2,3]
    random.shuffle(number)
    for i in range(1,4): 
        doors[f'door{i}'] = number[0]
        number.remove(doors[f'door{i}'])

    # Assign doors:
    winningDoorNum = random.randint(1,3)
    chosenDoor = random.randint(1,3)
    showDoor = random.randint(1,3)
    otherDoor = random.randint(1,3)

    # Check if doors are the same
    while True:
        if showDoor == winningDoorNum or showDoor == chosenDoor:
            showDoor = random.randint(1,3)
        else:
            break
    while True:
        if otherDoor == showDoor or otherDoor == chosenDoor:
            otherDoor = random.randint(1,3)
        else:
            break

    # Checks
    # print('other %s'%otherDoor)
    # print('chosen %s'%chosenDoor)
    # print('show %s'%showDoor)
    # print('winner %s'%winningDoorNum)

    # Points for the problem

    if chosenDoor == winningDoorNum:
        first = first + 1
    elif otherDoor == winningDoorNum:
        noFirst = noFirst + 1

print('Door selected %s' %(first*100/n))
print('Other door %s'%(noFirst*100/n))    

input()