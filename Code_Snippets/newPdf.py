import os, PyPDF2
os.chdir('D:/Drive/Code/ATBSWP/Chapter_13')
pdfFile = open('meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

resultPdf= open('result.pdf','wb')
pdfWriter.write(resultPdf)
pdfWriter.close()
resultPdf()
print('Done')
input()