import imapclient, pyzmail

#email
import sys
sys.path.insert(0, r'D:\Drive\Code\Random')
import file

myEmail = file.email

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(myEmail,file.test)
imapObj.select_folder('INBOX',readonly=True)
UIDs = imapObj.search(['SINCE', '05-Jul-2018'])
rawMessages = imapObj.fetch([8093],['BODY[]','FLAGS'])
test2 = rawMessages[8093]

message = pyzmail.PyzMessage.factory(rawMessages[8093][b'BODY[]'])
# message.get_subject()
# message.get_addresses('from')
# message.text_part != None
test = message.text_part.get_payload().decode(message.html_part.charset)
print(test)
imapObj.logout()
