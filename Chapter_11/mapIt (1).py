#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboar

import webbrowser, sys,pyperclip
if len(sys.argv) > 1:
    # Get aggress from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address form clipcboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

