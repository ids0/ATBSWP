import re, os, shutil

dateRegex = re.compile(r'''
        ^(.*?)              # Everything before    #Difference between (.*)?  Optional - (.*?)      Nongreedy)
        ([0|1][0-9])-       # Months Group 2
        ([0|1|2|3][0-9])-   # Days Group 3 
        ([0|1|2][0-9]{3})   # Years Group 4
        (.*?)$              # TODO: No space
        ''', re.VERBOSE)


print('Enter the folder to check')
folderToCheck = (r'%s' %(input()))
# folderToCheck = r"D:\Drive\Code\ATBSWP\Chapter_9"
# os.chdir(os.path.abspath(folderToCheck))
# os.chdir(r'\..')
# print(os.getcwd())

for folderName, subfoldersName, files in os.walk(folderToCheck):    # CWD does not include subfolders but renames folders not only files
    # print(subfoldersName)
    for subfolder in subfoldersName:
        mo3 = dateRegex.search(subfolder)
        if mo3 != None:
                newName = mo3.group(1)+mo3.group(3)+'-'+mo3.group(2)+'-'+mo3.group(4)+mo3.group(5)
                fromFile = os.path.join(folderName,mo3.group(0)) 
                toFile = os.path.join(folderName,newName)
                print('----- Renaming folder "%s" to "%s"\\... -----' %(fromFile,toFile))
                # shutil.move(fromFile,toFile)

    # """
    for file in files:
        # print(file)
        mo3 = dateRegex.search(file)
        if mo3 != None:
            newName = mo3.group(1)+mo3.group(3)+'-'+mo3.group(2)+'-'+mo3.group(4)+mo3.group(5)
            fromFile = os.path.join(folderName,mo3.group(0))    # mo3.group(0) = file = oldFileName
            toFile = os.path.join(folderName,newName)
            print('----- Renaming file "%s" to "%s"\\... -----' %(fromFile,toFile))
            # shutil.move(fromFile,toFile)

    # """
input()