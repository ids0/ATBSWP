#! python3
#mcb.pyw - MultiClipBoard

import pyperclip, os, sys, shelve
if (os.path.exists(r'.\mcb')) == False:
    os.makedirs(r'.\mcb')
os.chdir(r'.\mcb')
mcbShelf = shelve.open('mcb')
input()


if (len(sys.argv) == 3) and sys.argv[1] == 'save':
    key = sys.argv[2]
    content = str(pyperclip.paste())
    mcbShelf[key] = content
elif (len(sys.argv) == 2) and sys.argv[1] == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
    print(list(mcbShelf.keys()))
    print(list(mcbShelf.values()))
elif (len(sys.argv) == 2) and sys.argv[1] in mcbShelf:
    pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()