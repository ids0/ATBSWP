import re
dateRegex = re.compile(r'''
        ^(.*?)              # Everything before    #Difference between (.*)?  Optional - (.*?)      Nongreedy)
        ([0|1][0-9])-    # Months Group 2
        ([0|1|2|3][0-9])-  # Days Group 3 
        ([0|1|2][0-9]{3})   # Years Group 4
        (.*?)$              # TODO: No space
        ''', re.VERBOSE)


datePattern = re.compile(r'''
    ^(.*?) # all thext before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
    ''', re.VERBOSE)

test = 'A13-21-2018Spam Test - Copy.txt'
test2 = '04-24-2018'
mo1 = dateRegex.search(test)
print(mo1.group(4))
input()