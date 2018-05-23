def spam():
    global eggs
    eggs = 'spam'   # this is the global

def bacon():
    eggs = 'bacon'  # this is a local

def ham():
    print(eggs)     # this is the global

eggs = 42           # this is the global
ham()               # prints eggs global before it's reasignment
spam()              # reasign eggs to spam
ham()               # prints new eggs
bacon()             # does nothing
print(eggs)         # prints new eggs
input()