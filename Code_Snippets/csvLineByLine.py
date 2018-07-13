import os
import csv
os.chdir(r'D:\Drive\Code\ATBSWP\Chapter_14')
# Create file
outputFile = open('output.csv', 'w', newline='')

outputWriter = csv.writer(outputFile, delimiter=',', lineterminator='\n')  # defaults delimiter and lineterminator
lst1 = ['spam', 'eggs', 'bacon']
lst2 = ['Hello, world!', ' eggs', 'ham']
lst3 = ['1', '3.141592', '4', '4']
outputWriter.writerow(lst1)
outputWriter.writerow(lst2)
outputWriter.writerow(lst3)
outputFile.close()
# Open
file = open('output.csv')
fileReader = csv.reader(file)
for row in fileReader:
    print('Row #' + str(fileReader.line_num) + ' ' + str(row))

for x in range(1, 10):
    print(x)
    pass
