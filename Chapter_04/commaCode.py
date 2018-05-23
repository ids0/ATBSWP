import copy
def commaCode(aList):
    newList = copy.copy(aList)
    items = ''
    for item in range(len(newList)):
        if item == 0:
            items = str(newList[item])
        elif item == len(newList)-1:
            items = items + ' and ' + str(newList[item])
        else:
            items = items + ', ' + str(newList[item])
    return items

spam = ['apples', 'bananas','tofu','cats', 1, True, 'test', ['test2','test3']]
print(commaCode(spam))
input()
        
    