import zipfile, os, re
text = 'YO10-05-2018, 11-30-2018'
datesRegex = re.compile(r'''(
        .*?           # Everything before    #TODO: Difference between (.*)? and (.*?)
        ([0|1][0|1|2])  # Months
        -
        ([0|1|2|3][0-9])    # Days
        -
        ([0|1|2][0-9]{3})   # Years
        .*?
        )''', re.VERBOSE)
mo = datesRegex.findall(text)
print(mo[1])


input()