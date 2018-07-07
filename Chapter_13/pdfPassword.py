#! python3
# pdfPassword.py - Bruteforce password for a pdf file

import os, PyPDF2

os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_13')
file = r'D:\Drive\Code\ATBSWP\Chapter_13\Encrypted\watermark_encrypted.pdf'
passwordFile = open('dictionary.txt', 'r').readlines()
passwords = []
for line in range(len(passwordFile)):
    passwords.append(passwordFile[line][:-1])   # Get rid of /n

lst = []
for i in passwords:
    if i[0] not in lst:
        lst.append(i[0])
        print('working with words %s' %i[0])
    pdfFile = open(file,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    if pdfReader.decrypt(i) == 1:
        print('Done, passwrod is %s'%i)
        break
    if pdfReader.decrypt(i.lower()) == 1:
        print('Done, passwrod is %s'%i.lower())
        break
    
print('out of loop')
input()