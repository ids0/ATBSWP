def printPicnic(itemsDict, leftWith, rightWidth):
    print('PICNIC ITEMS'.center(leftWith + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWith,'.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 800}
printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)
input()