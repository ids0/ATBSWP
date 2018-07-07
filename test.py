import os, PyPDF2

os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_13')
file = r'D:\Drive\Code\ATBSWP\Chapter_13\Encrypted\watermark_encrypted.pdf'
pdfFile = open(file,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
test = pdfReader.isEncrypted
print(test)
test2 = pdfReader.decrypt('test')
print(test2)
test = 'hola'
print(test[0])