import subprocess

fileObj = open(r'D:\Drive\Code\ATBSWP\Chapter_15\hello.txt','w')
fileObj.write('Hello world!')
fileObj.close()
subprocess.Popen(['start','D:\Drive\Code\ATBSWP\Chapter_15\hello.txt'], shell=True)
