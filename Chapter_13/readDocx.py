#! python3

import docx,os
os.chdir('D:/Drive/Code/ATBSWP/Chapter_13')
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for p in doc.paragraphs:
        fullText.append(p.text)
    return '\n'.join(fullText)