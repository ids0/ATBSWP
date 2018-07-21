from ftplib import FTP

ftp = FTP('192.168.1.102:3248')
ftp.login(user='ivan',passwd='ivan')
print(ftp.retrlines('LIST'))