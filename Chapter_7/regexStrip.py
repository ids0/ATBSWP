import re
print('Enter text to scan')
string = input()
print('Enter world to be replace (space is default)')
testErase = input()
def stripRegex(string,erase = ''):
    if erase == '':
        erase = ' '
    elif erase == '*':
        erase = '\*'
    elif erase == '.':
        erase = '\.'
    elif erase == '(':
        erase = '\('
    else:
        pass

    stripRegex = re.compile(r'''(^(%s)*|(%s)*$)''' %(erase,erase))  # Can't make regex work with re.VERBOSE 
    mo = stripRegex.sub(r'',string)
    
    return mo
mo1 = stripRegex(string,testErase)
print('NoSpace-' + mo1 + '-MoSpace')
input()