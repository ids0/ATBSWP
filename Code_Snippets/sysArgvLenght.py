import sys
#First checks the lenght of sys.argv to know what todo, if len(sys.argv) == 3 returns False, the second condition is not executed
aList = []
if (len(sys.argv) == 3) and sys.argv[1] == '1st Argument' and sys.argv[2] == '2nd Argument':
    pass
elif (len(sys.argv) == 2) and (sys.argv[1] in aList):
    pass
elif (len(sys.argv) == 2) and sys.argv[1] == 'Only Argument':
   pass

if len(sys.argv) > 2: # file name and something
    something = ' '.join(sys.argv[1:])  # adds every arguments after the file name to 1 string 