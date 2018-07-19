#! python3
# randomChore.py - 

import random,smtplib
import sys
sys.path.insert(0, r'D:\Drive\Code\Random')
import file



chores = ['Chore1', 'Chore2', 'Chore3','Chore4']
random.shuffle(chores)
emails = ['email1@testofemail.com', 'email2@testofemail.com','email3@testofemail.com', 'email4@testofemail.com']

myEmail = file.email
smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(myEmail,file.test)

for i in range(len(chores)):
    # send email
    body = f"Subject: Weekly chore.\nThis week you have to {chores[i]}"
    emailTo = emails[i]
    print(f'Sending email to {emailTo}')
    sendMailStatus = smtpObj.sendmail(myEmail,emailTo,body)

    if sendMailStatus != {}:
        print(f'There was a problemn sending email to {emailTo}: {sendMailStatus}')

    # print(f'Sending {body} to {emailTo}')

smtpObj.quit()

    
    
   
