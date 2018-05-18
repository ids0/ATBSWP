import os,zipfile
os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_9\test')
# toBackup = r'%s' % input()
toBackup = r'D:\Drive\Code\ATBSWP\Chapter_9\test'
foldertoBackup = os.path.split(toBackup)[1]
this = foldertoBackup+'.zip'
# newZip = zipfile.ZipFile('%s' %this,'w')
for files in os.listdir(toBackup):
    filePath = os.path.join(toBackup,files)
    
         
input()