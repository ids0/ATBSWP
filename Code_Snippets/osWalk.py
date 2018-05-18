import os

print('Enter the folder to check')
# folderToCheck = (r'%s' %(input()))
folderToCheck = r"D:\Drive\Code\ATBSWP\Chapter_9"
# os.chdir(os.path.abspath(folderToCheck))
# os.chdir(r'\..')
# print(os.getcwd())

for folderName, subfoldersName, files in os.walk(folderToCheck):    # CWD does not include subfolders but renames folders not only files
    print(subfoldersName)
    for subfolder in subfoldersName:
        print('Folder:' + folderName)                   # D:\Drive\Code\ATBSWP\Chapter_9
        print('Subfolder: ' + subfolder)                # test_folder
        subfolderPath = os.path.join(folderName,subfolder) # D:\Drive\Code\ATBSWP\Chaptor_9\test_folder

    for file in files:
        print('Folder:' + folderName)                   # D:\Drive\Code\ATBSWP\Chapter_9\test_folder
        print('File: ' + file)                          # file.txt
        filePath = os.path.join(folderName,file)        # D:\Drive\Code\ATBSWP\Chapter_9\test_folder\file.txt

input()