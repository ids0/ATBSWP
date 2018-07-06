import os, re, shutil 
folder = r'D:\LOCATION'

nameRegex = re.compile(r"""
    (.*)                #   group(1)
    (\s_TEXT1\sTEXT2)   #   ' _TEXT1 TEXT2" /s == ' '
    (.*)                #   group(3)
    """, re.X)          #   re.X == re.VERBOSE

for file in os.listdir(folder):
    ren = nameRegex.search(file)
    if ren != None:
        newName = ren.group(1)+ren.group(3)+'.mp4'
        fileFrom =  os.path.join(folder,file)
        fileTo =    os.path.join(folder,newName)
        print('Moving %s to %s' %(fileFrom, fileTo))
        # shutil.move(fileFrom, fileTo)
