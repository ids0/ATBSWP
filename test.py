import os
# totalSize = 0
# for filename in os.listdir('C:\\Windows\\System32'):
#     totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32',filename))
# print(totalSize)

helloFile = open('D:\Drive\Code\ATBSWP\Chapter_8\\hello.txt')
print(helloFile.read())
helloFile.close()
sonnetFile = open(('D:\Drive\Code\ATBSWP\Chapter_8\\sonnet29.txt'))
print(sonnetFile.readlines())
input()