#! python3
# excelToCsv.py -

import os, csv, openpyxl
os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_14\Test')

#name = filename_sheet.csv

for file in os.listdir('.'):
    if not file.endswith('.xlsx'):
        continue
    print('working with %s'%file)
    # Load xlsx file
    wb = openpyxl.load_workbook(file, data_only=True)
    # Load xlsx sheet
    sheets = wb.sheetnames
    for sheet in sheets:
        ws = wb[sheet]
         # create CSV file
        newName = file[:-5] + '_' + sheet + '.csv'
        outputFile = open(newName,'w',newline='')
        outputWritter = csv.writer(outputFile)
        for rowNum in range(1,ws.max_row+1):
            values = []
            for colNum in range(1,ws.max_column+1):
                # read sheet content
                cell = ws.cell(row=rowNum, column=colNum).value
                values.append(cell)
            print(values)
            outputWritter.writerow(values)
        outputFile.close()
                