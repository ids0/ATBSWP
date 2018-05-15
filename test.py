import zipfile, os, re
text = 'YO10-05-2018.docs, 91-30-2018'
datesRegex = re.compile(r'''(
        ^(.*?)           # Everything before    #Difference between (.*)?  Optional - (.*?)      Nongreedy
        ([0|1][0|1|2])  # Months Group 2
        -
        ([0|1|2|3][0-9])    # Days Group 3 
        -
        ([0|1|2][0-9]{3})   # Years Group 4
        (.*?) #no space
        )''', re.VERBOSE)
mo = datesRegex.search(text)
print(mo.group())
newName = str(mo.group(2))+str(mo.group(4))+'-'+str(mo.group(3))+'-'+str(mo.group(5))+str(mo.group(6))
print(newName)

datePattern = re.compile(r'''^(.*?) # all thext before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
    ''', re.VERBOSE)

mo2 = datePattern.search(text)
print('Here comes MO2')
print(mo2.group)    
print('That was dissapointing')


for folderName, subfoldersName, files in os.walk('.\Chapter_9'):    # CWD does not include subfolders but renames folders not only files
    for file in files:
        print(folderName +'\\'+ str(file))      # TODO: Function join
        mo3 = datePattern.search(file)
        if mo3 != None:
                print('---Do---')
                print(mo3)


input()