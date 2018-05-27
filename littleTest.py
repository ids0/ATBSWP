import os, re, glob
Location = r'C:\Users\Ivan\Desktop'


listing = glob.glob('C:/foo/bar/foo.log*')
for filename in listing:
    # do stuff
    pass


testRegex = re.compile(r'''2018-05-27--10-39-01_NJH47F_release-keys''')
text = '2018-05-27--10-39-01_NJH47F_release-keys'
mo = testRegex.search(text)


for files in os.listdir(Location):
    print(files)
    mo = testRegex.search(files)
if mo != None:
    print(mo)
    print('MOOOOO')
else:
    print()
# print(mo.group())
input()