import copy

def eggs(someParameter):
    newParameter = copy.copy(someParameter)


    
    newParameter.append('Hello')
    print(newParameter)

spam = [1,2,3]
eggs(spam)
print(spam)
input()