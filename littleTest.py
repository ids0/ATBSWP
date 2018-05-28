import os, re

titaniumRegex2 = re.compile(r'''
    TitaniumBackup
    \s?
    (\d{2})-?   # group 1
    (\d{2})-?    # group 2
    (\d{4})?     # group 3
    [^ ]*
    ''', re.VERBOSE)

text = 'New folder TitaniumBackup 19-05-2018 TitaniumBackup 20-05-2018 TitaniumBackup 27-05-2018'

tbLen = len(titaniumRegex2.findall(text))
print(titaniumRegex2.findall(text))
input()