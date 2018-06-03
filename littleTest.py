import os
for foldersPath, subfoldersName, fileNames in os.walk(r'D:\Drive\Code\ATBSWP'):
    # print(foldersPath)
    pass
    # break
    for subfolder in subfoldersName:
        pass
        # print(subfolder)
        for filename in fileNames:
            print(filename)
            pass
for folder in os.listdir(r'D:\Drive\Code\ATBSWP'):
    break
    print(folder)
input()