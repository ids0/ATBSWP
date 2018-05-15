#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re
# newCWD= input()
# os.chdir(r'%s' %(newCWD))
# Create a regex that matches files with the American date format.
datePattern = re.compile(r'''^(.*?) # all thext before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
    ''', re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):    # CWD does not include subfolders but renames folders not only files
    mo = datePattern.search(amerFilename)
    print(amerFilename)
    # Skip files  or folders without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart  = mo.group(1) 
    monthPart   = mo.group(2)
    dayPart     = mo.group(4)
    yearPart    = mo.group(6)
    afterPart   = mo.group(8)
    # Form the European=style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)


    # Rename the files.
    print('Renaming ' '%s' ' to ' '%s' '...' % (amerFilename,euroFilename))
    #shutil.move(amerFilename,euroFilename) # uncomment after testing

