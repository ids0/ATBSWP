import os, PyPDF2
os.chdir('D:/Drive/Code/ATBSWP/Chapter_13')
minutesFile = open('meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.getNumPages()):
    pageObj = pdfReader.getPage(pageNum).rotateClockwise(90*(pageNum+1))
    pdfWriter.addPage(pageObj)


resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()

input()