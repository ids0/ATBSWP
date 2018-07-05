#! python3
# mapIt.py
import webbrowser, sys, pyperclip
if len(sys.argv) > 1 :
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()


link = 'www.google.com/maps/place/'
completeLink = link + address
# print(completeLink)
# input()
webbrowser.open(completeLink)
