#! python3
# renameDates2.py  - First try of renameDates without looking the code first
import re, os, shutil
path = ''
# TODO: Search filenames in all subfoldes from one folder
    # TODO: Regex to find dates FROM MM-DD-YYYY to DD-MM-YYYY
text = 'YO10-05-2018.docs, 11-30-2018'
datesRegex = re.compile(r'''(
        (.*?)           # Everything before Group 2    #Difference between (.*)?  Optional - (.*?)      Nongreedy
        ([0|1][0|1|2])  # Months Group 3
        -
        ([0|1|2|3][0-9])    # Days Group 4 
        -
        ([0|1|2][0-9]{3})   # Years Group 5
        (.*?)               # Everything afterGroup 6
        )''', re.VERBOSE)
mo = datesRegex.findall(text)
print(mo)
    # TODO: List of the filenames 
for folderName, subFolders, filenames in os.walk(path):
    for filename in filenames:
        if filename in datesRegex(text):
            newName = ''
            shutil.move(filename,'.\\%s\\%s' % (folderName,newName))
            print(filename,'.\\%s\\%s' % (folderName))

# TODO: When a file is found it is renamed with the European-style