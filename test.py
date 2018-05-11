import os
# totalSize = 0
# for filename in os.listdir('C:\\Windows\\System32'):
#     totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32',filename))
# print(totalSize)

# helloFile = open(r'D:\Drive\Code\ATBSWP\Chapter_8\hello.txt','w')
# print(helloFile.read())
# helloFile.close()
# sonnetFile = open((r'D:\Drive\Code\ATBSWP\Chapter_8\sonnet29.txt'),'a')
# print(sonnetFile.readlines())
os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_8')
baconFile = open('bacon.txt','w')
baconFile.write('Hello world!\n')
baconFile.close()
input()