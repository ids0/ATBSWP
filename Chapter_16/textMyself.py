#! python3
# textMyself.py - Defines the textmyself() function that text a message
# passeed to it as a string.

import sys
sys.path.insert(0, r'D:\Drive\Code\Random')
import file

# Preset values:
accountSID = file.account_sid
authToken = file.auth_token
myNumber = file.myCellPhone
twilioNumber = file.myTwilioNumber

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID,authToken)
    twilioCli.messages.create(body=message,from_=twilioNumber,to=myNumber)