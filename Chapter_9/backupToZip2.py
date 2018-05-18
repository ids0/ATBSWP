#! python3
# backuptoZip2.py - Personal version of backupToZip.py
# TODO: Comment the code
# TODO: Use shelve module to save last index
# TODO: Somethin first time running -> no test.zip
import os,zipfile,re

# toBackup = r'%s' % input()
toBackup = r'D:\Drive\Code\ATBSWP\Chapter_9\test'
os.chdir(toBackup)
foldertoBackup = os.path.split(toBackup)[1] # folder to backup 'folder_name'

# Regex to look the version
VersionRegex = re.compile(r'''
    (%s)
    _?
    (\d?)
    .zip
    '''%foldertoBackup,re.VERBOSE)

# Loop in the folder

dirTolook = os.listdir(toBackup)
allVer = []
for files in dirTolook:
    mo = VersionRegex.search(files)
    if mo != None:
        allVer = allVer + [mo.group()]
        # print(mo.group(2))
if VersionRegex.search(allVer[-1]).group(2) == '':
    lastVersion = 0
else:
    lastVersion = VersionRegex.search(allVer[-1]).group(2)


zipName = foldertoBackup+'_'+str(int(lastVersion)+1)+'.zip'
newZip = zipfile.ZipFile('%s' %zipName,'w')

for files in dirTolook:
    newZip.write(files,compress_type=zipfile.ZIP_DEFLATED)

newZip.close()

print('Done')
input()