#! python3
# pw.py - An insecure password locker program.
PASSWORDS = {'email': 'password1',
            'blog':'password2',
            'luggage':'12345'}

import sys,pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit() 
    
print(sys.argv)    
account = sys.argv[1] # first command line arg is the account name 

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Passsword for ' + account + ' copied to clipboard.')
else:
    print('The is no account named '+ account)
input()