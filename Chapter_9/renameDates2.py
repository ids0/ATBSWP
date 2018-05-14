#! python3
# renameDates2.py  - First try of renameDates without looking the code first
import re, os
# TODO: Search filenames in all subfoldes from one folder
    # TODO: Regex to find dates FROM MM-DD-YYYY to DD-MM-YYYY
text = '12-05-2018, 11-30-2018'
datesRegex = re.compile(r'''(
        (.*)+           # Everything before    
        ([0|1][0|1|2])  # Months
        -
        ([0|1|2|3][0-9])    # Days
        -
        ([0|1|2][0-9]{3})   # Years
        )''', re.VERBOSE)
mo = datesRegex.findall(text)
print(mo)
    # TODO: List of the filenames 

# TODO: When a file is found it is renamed with the European-style