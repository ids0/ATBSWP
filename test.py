#! python3
# phoneBackup.py - Moves the te nandroid baackup folder and the TitaniumBackup folder to the hardrive
# then renames the new TitaniumBackup folder and deletes the old version of nandroid and TitaniumBackup
# folders

import os, datetime, shutil, send2trash, re
nanBackupFolder = r'D:\Ivan\Android\OP 3T\Nandroid'
tbBackupFolder = r'D:\Ivan\Android\OP 3T\TitaniumBackup'
# Regex of names
titaniumRegex = re.compile(r'''^TitaniumBackup$''', re.VERBOSE)
nanRegex = re.compile(r'''
    (\d{4})-
    (\d{2})-
    (\d{2})
    --
    (.*)*
    ''',re.VERBOSE)

# New Regex for dates and all
titaniumRegex2 = re.compile(r'''
    ^TitaniumBackup
    \s
    (\d{2})-    # group 1
    (\d{2})-    # group 2
    (\d{4})     # group 3
    ''', re.VERBOSE)
nanRegex2 = re.compile(r'''
    (\d{4})-
    (\d{2})-
    (\d{2})
    --
    (.*)*
    ''',re.VERBOSE)

# search the folders
location = r'C:\Users\Ivan\Desktop'
for files in os.listdir(location):
    # Nandroid
    nan = nanRegex.search(files)
    # Move folder
    if nan != None:
        print(nan.group())
        fileFrom = os.path.join(location,files)
        fileTo = os.path.join(nanBackupFolder,files)
        print('Moving %s to %s' %(fileFrom, fileTo))
        shutil.move(fileFrom, fileTo)
    else:
        print('Nope')
    # Titanium
    tb = titaniumRegex.search(files)
    # Move and rename folder
    if tb != None:
        print(tb.group())
        # Rename TitaniumBackup
        now = datetime.datetime.now()   # Get date
        date = now.strftime('%d-%m-%Y') # Date format
        newName = files + ' ' + date    # TitaniumBackup DD-MM-YYYY
        fileFrom = os.path.join(location,files)
        fileTo = os.path.join(tbBackupFolder,newName)
        print('Moving %s to %s' %(fileFrom, fileTo))
        shutil.move(fileFrom, fileTo)
    else:
        print('Nope again')


# Delete oldfolders
if len(os.listdir(tbBackupFolder)) > 2:
    print('2 many files') 
    lst = []
    for files in os.listdir(tbBackupFolder):
        tb = titaniumRegex2.search(files)
        if tb != None:
            sumDate = (int(tb.group(1))*1+int(tb.group(2))*100000+int(tb.group(3))*100000000)
            lst = lst + [[files, int(tb.group(1)), int(tb.group(2)), int(tb.group(3)), sumDate]]
            # tb.group(1) #day
            # tb.group(2) #month
            # tb.group(3) #year
    print(lst)
            # lst[i][0]  file name
            # lst[i][1]  day
            # lst[i][2]  month
            # lst[i][3]  year
            # lst[i][4]  sumDate # mayor mas nuevo
    checkSum = lst[1][4]
    older = lst[1][0]
    for i in range(len(lst)):
        if  lst[i][4] < checkSum:
            checkSum = lst[i][4]
            older = lst[i][0]
    olderPath = os.path.join(tbBackupFolder,older)

    send2trash.send2trash(olderPath)
    print('%s in trash' % olderPath)
else:
    print('Only 2 backups')
input()