import os, re, shutil 
folder = r'D:\LOCATION'

nameRegex = re.compile(r"""
    (.*)                #   group(1)
    (\s_TEXT1\sTEXT2)   #   ' _TEXT1 TEXT2"
    (.*)                #   group(3)
    """, re.X)

# nameRegex = re.compile(r'''(.*)( _TEXT1 TEXT2_)(.*)''')

for file in os.listdir(folder):
    ren = nameRegex.search(file)
    # print(ren)
    if ren != None:
        # print(ren.group(1))
        newName = ren.group(1)+ren.group(3)
        # newName = 'test'
        # print(newName)
        fileFrom =  os.path.join(folder,file)
        fileTo =    os.path.join(folder,newName)
        print('Moving %s to %s' %(fileFrom, fileTo))
        # shutil.move(fileFrom, fileTo)
