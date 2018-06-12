#! python3
# updateProduceV2 - 
import os, openpyxl
os.chdir('D:/Drive/Code/ATBSWP/Chapter_12')
print('Loading worksheet...')
wb = openpyxl.load_workbook('produceSales.xlsx')
ws = wb[wb.sheetnames[0]]

# Loop every row
print('Working')
for i in range(2,ws.max_row):
    # Check if the value is
    if ws.cell(row=i,column=1).value == 'Celery':
        ws[ws.cell(row=i,column=2).coordinate] = 1.19
    elif ws.cell(row=i,column=1).value == 'Garlic':
        ws[ws.cell(row=i,column=2).coordinate] = 3.07
    elif ws.cell(row=i,column=1).value == 'Lemon':
        ws[ws.cell(row=i,column=2).coordinate] = 1.27

# Save
wb.save('produceSalesV2.xlsx')

print('Done')
input()
