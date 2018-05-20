#! python3
# backuptoZip2.py - Personal version of backupToZip.py


import os,zipfile,re

# toBackup = r'%s' % input()    # Allows the user to input the directory to backup
toBackup = r'D:\Drive\Code\ATBSWP\Chapter_9\test'   # Test directory
os.chdir(toBackup)
foldertoBackup = os.path.split(toBackup)[1] # folderToBackup = 'folder_name', sabe as os.path.basename(toBackup)

# Regex to look the version
VersionRegex = re.compile(r'''
    (%s)
    _?
    (\d?)
    .zip
    '''%foldertoBackup,re.VERBOSE)

# Loops in the folder
dirTolook = os.listdir(toBackup) # Lists the content of the folder to iterate everyone 

# Search for the last version
allVer = []
for files in dirTolook:
    mo = VersionRegex.search(files)
    if mo != None:
        allVer = allVer + [mo.group()]  # allVer is a list of versions
        # print(mo.group(2))

if allVer == []:    # first time running
    lastVersion = 0
else:               
    lastVersion = VersionRegex.search(allVer[-1]).group(2)  # Last version is the last of the list, pass the Regex group(2) to find the version number

# Create the new zip
zipName = foldertoBackup+'_'+str(int(lastVersion)+1)+'.zip'
newZip = zipfile.ZipFile('%s' %zipName,'w')


for files in dirTolook: # Adds the files to the newZip
    if (files+'_').startswith(foldertoBackup) and files.endswith('.zip'): # skips the previous backups
        continue
    else:
        print('Adding %s ' % files)
    newZip.write(files,compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


print('Done')
input()