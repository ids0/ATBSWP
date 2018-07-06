#! python3
# PDFParanoia.py - Goes through ever PDF in a folder (and subfolders) and encrypt the PDFs

import os, PyPDF2, sys, send2trash

while True:
# if len(sys.argv) > 2:     # TODO: Use sys.argv
    password = 'test'
    folder = r'D:\Drive\Code\ATBSWP\Chapter_13'
    os.chdir(folder)
    # Create new directory if it doesn't exist
    saveTo = folder + r'\Encrypted'
    os.makedirs('Encrypted', exist_ok=True)
    os.chdir(saveTo)

    for pdf in os.listdir(folder):
        if pdf.endswith('.pdf'):
            print('Working with %s'%pdf)
            pdfLocation = os.path.join(folder,pdf)
            # Open pdf file
            pdfFile = open(pdfLocation,'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            if pdfReader.isEncrypted:
                print('%s is already encrypted'%pdf)
            else:
                # Write new pdf
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                # Encrypt new pdf
                pdfWriter.encrypt(password)
                # Create new pdf file
                newPDFName = pdf[:-4] + '_encrypted.pdf'    # cut .pdf at the end of original file name
                newPDF = open(newPDFName, 'wb')
                pdfWriter.write(newPDF)
                newPDF.close()
                print('%s created'%newPDFName)
                # Check if new pdf is encrypted and delete old pdf
                newPDFLocation = os.path.join(saveTo,newPDFName)
                newPDFFile = open(newPDFLocation,'rb')
                newPDFReader = PyPDF2.PdfFileReader(newPDFFile)
                if newPDFReader.isEncrypted and newPDFReader.decrypt(password) == 1:    # check if the encryption worked and tries to decrypt
                    print('Deleting %s'%pdfLocation)
                    # send2trash.send2trash(pdfLocation)
                else:
                    print('%s isn\'t encrypted correctly'%pdf)
            print('')

    break