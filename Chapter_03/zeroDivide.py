def spam(divideBy):
    try:
        return 42 / divideBy
    except:
        print('Error: Invalid shit.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam('nice'))
print(spam(1))
test = input()