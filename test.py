import os, docx
os.chdir('D:/Drive/Code/ATBSWP/Chapter_13')
doc = docx.Document('demo.docx')
# print(doc.paragraphs[1].runs[0].text)
for p in range(len(doc.paragraphs)):
    for r in range(len(doc.paragraphs[p].runs)):
        print(doc.paragraphs[p].runs[r].text,end='')
    print('')

input()