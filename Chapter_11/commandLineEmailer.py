#! python3
# commandLineEmailer - send a Email form the command line

# TODO: Make something usefull of this shit, maybe test results?
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# if len(sys.argv) < 3:
    # print('Please enter an email and the message')
if False:
    pass
else:
    print('Enter your email')
    myEmail = input()
    print('Enter your password')
    myPass = input()
    # sendTo = sys.argv[1]
    sendTo = 'testemail@gmail.com'
    # message = ' '.join(sys.argv[2:])
    message = 'test message'

    # TODO: show message and recipient to confirm
    print(message)
    print('Do you really want to send an email to %s' %sendTo)
    print('''
        %s
        '''%message)
    print('y to follow n to abort')
    # sure = input()
    sure = 'Y'
    if sure.lower() == 'n':
        print('Abort!')
    elif sure.lower() == 'y':
        print('Sending the message')
        print('Opening browser')
        browser = webdriver.Firefox()
        browser.get('http://gmail.com')
        browser.find_element_by_id('identifierId').send_keys(myEmail)
        browser.find_element_by_id('identifierNext').click()
        try:
            element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        finally:
            pass
        browser.find_element_by_id('password').send_keys(myPass)
    else:
        pass


input()
browser.quit()