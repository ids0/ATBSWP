import os, openpyxl
os.chdir('D:/Drive/Code/ATBSWP/Chapter_12')
wb = openpyxl.load_workbook('produceSales.xlsx')
ws = wb[wb.sheetnames[0]]
print()
input()
