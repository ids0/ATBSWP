#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for
# each county.

import openpyxl, pprint, os
os.chdir('D:/Drive/Code/ATBSWP/Chapter_12')
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

# TODO: Fill in countyData with each county's population and tracts
print('Reading Rows...')
for row in range(2,sheet.max_row+1):
    # Each row in the spreadsheet has data for one census tract.
    state   = sheet['B' + str(row)].value
    county  = sheet['C' + str(row)].value
    pop     = sheet['D' + str(row)].value

    # Make sure the key for this county in this state exists.
    

# TODO: Open a new text file and write de contents of countyData to it 
input()