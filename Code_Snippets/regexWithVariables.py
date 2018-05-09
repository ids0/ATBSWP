import re
string = 'text to scan'
erase = 'something at the beginning'
erase2 = 'something else at the end'
stripRegex = re.compile(r'''(^(%s)*|(%s)*$)''' %(erase,erase)) 
mo = stripRegex.sub(r'',string)
    
input()