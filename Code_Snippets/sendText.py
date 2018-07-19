from twilio.rest import Client

import os, sys
os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_16')
sys.path.insert(0, r'D:\Drive\Code\Random')
import file

account_sid = file.account_sid
auth_token  = file.auth_token
myCellPhone = file.myCellPhone
myTwilioNumber = file.myTwilioNumber

client = Client(account_sid, auth_token)
message = client.messages.create(to=myCellPhone, from_=myTwilioNumber,body='Texting test text')
print(message.status)
