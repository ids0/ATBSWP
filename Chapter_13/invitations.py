#! python3
# invitations.py

import os, docx
os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_13')
# Put guests names on a list
guests = open('guests.txt','r').readlines()
# Create document
doc = docx.Document('styles.docx')
for name in guests:

    obj1 = doc.add_paragraph('It would be a pleasure to gave the company of','Heading1')
    obj1.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER

    obj2 = doc.add_paragraph(name[:-1], 'Title')
    obj2.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    obj2.runs[0].bold = True

    obj3 = doc.add_paragraph('at 11010 Memory Lane on the Evening of', 'Style1')
    obj3.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    obj3.runs[0].italic = True

    obj4 = doc.add_paragraph('April 1st')
    obj4.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER

    obj5 = doc.add_paragraph('at 7 o\'clock')
    obj5.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER

    doc.add_page_break()

doc.save('invitations.docx')