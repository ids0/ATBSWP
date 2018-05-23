def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
print(eggs)     # prints 'global'
spam()
print(eggs)     # prints 'spam'
input()