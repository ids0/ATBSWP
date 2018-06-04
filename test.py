# from selenium import webdriver
# import pprint
# print('Opening Firefox...')
# browser = webdriver.Firefox()
# browser.get('http://inventwithpython.com')
# linkElem = browser.find_elements_by_link_text('Read Online for Free')
# print(type(linkElem))
# linkElem[1].click()    # follows the "Read It Online" link
# pprint.pprint(linkElem)
# input()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# print('Opening Firefox...')
# browser = webdriver.Firefox()
# browser.get('http://gmail.com')
# emailElem = browser.find_element_by_id('identifierId')
# emailElem.send_keys('Email@gmail.com')
# nextButtonElem = browser.find_element_by_id('identifierNext')
# nextButtonElem.click()
# for i in range(1220000):
#     i = i + 1
#     if i % 1000 == 0:
#         print(int(i/1000))
#     pass
# passwordElem = browser.find_element_by_tag_name('html')
# passwordElem.send_keys('Du')
# # passwordElem.submit()
# input()

import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select