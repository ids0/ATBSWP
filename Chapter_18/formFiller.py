#! python3
# formFiller.py - Automatically fills in the form.

import pyautogui,time

# Set these to the correct coordinates for your computer.
nameField = (835,375)
submitButton = (858,898)
submitButtonColor = ( 72, 136, 239)
submitAnotherLink = (957,276)

formData = [{'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
            {'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
            ]

pyautogui.PAUSE = 0.5

for person in formData:
    # Give the user a chance to kill the script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    for i in range(5):
        time.sleep(1)
    
    # Wait until the form page has loaded
    while not pyautogui.pixelMatchesColor(submitButton[0],submitButton[1],submitButtonColor):
        time.sleep(0.5)
        print('sleping...')
        
    print(f'Entering {person["name"]} info...')
    pyautogui.click(nameField[0],nameField[1])

    # Fill out the name Field.
    pyautogui.typewrite(person['name'] + '\t')

    # Fill Out the Greates Fear(s) field.
    pyautogui.typewrite(person['fear'] + '\t')

    # Fill out the Source of Wizard Powers field.
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])
    elif person['source'] == 'amulter':
        pyautogui.typewrite(['down','down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down','down','down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down','down','down','down', '\t'])

    # Fill out the RoboCop field.
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right','right' , '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right','right' ,'right' , '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right','right' ,'right' ,'right' , '\t'])

    # Fill out the Additional Comments field.
    pyautogui.typewrite(person['comments'] + '\t')

    # Click Submit.
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Clicked Submit.')
    for i in range(5):
        time.sleep(1)
    
    # Click the Submit another response link.
    pyautogui.click(submitAnotherLink[0],submitAnotherLink[1])
