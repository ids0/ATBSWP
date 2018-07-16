import smtplib


# smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)
smtpObj = smtplib.SMTP('smtp-mail.outlook.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('isnow78@hotmail.com',input())
smtpObj.sendmail('isnow78@hotmail.com','ivandrelichman@gmail.com','Subject: Test.\nTest')
# print(test)