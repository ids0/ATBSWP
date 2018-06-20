import os, docx
os.chdir('D:/Drive/Code/ATBSWP/Chapter_13')
doc = docx.Document('demo.docx')
para = doc.paragraphs
for p in para:
    print(p.text)
input()