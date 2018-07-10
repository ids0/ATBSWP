#! python3
# removeCsvHeader.py - Removes the header for all CSV files in the currrent working directory

import csv, os
os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_14\removeCsvHeader')

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory
for csvFileName in os.listdir('.'):
    if not csvFileName.endswith('.csv'):
        continue    # skip non-csv files
    
    print('Removing header from %s ...' %csvFileName)

    # Reade the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(csvFileName)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue    # skip first row
        csvRows.append(row)
    csvFileObj.close()

    # Write out the CSV file.
    csvFilePath = os.path.join('headerRemoved', csvFileName)
    csvFileObj = open(csvFilePath,'w',newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()