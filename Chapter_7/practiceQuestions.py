import re
# 20
print('------20------','\n')
text = ['1,23','42','1,234','6,368,745','12,34,567','1234']
for item in text:
    numsRegex = re.compile(r'''(
        (^\d{1,3})      # Expresion n
        (,\d{3})*$      # Expresion n
        )''', re.VERBOSE)
    mo20 = numsRegex.findall(item)
    if mo20 != []:
        print(mo20)

# 21
print('\n','------21------','\n')
text = ['Satosh Nakamoto','Alice Nakamoto','RoboCop Nakamoto','satoshi Nakamoto','Mr. Nakamoto','Nakamoto', 'Satoshi nakamoto', 'A Nakamoto', 'a Nakamoto', 'A5 Nakamoto']
for item in text:
    numsRegex = re.compile(r'''(
        ([A-Z])         # Name that beggins with uppercase
        ([a-z]*)        # 0 or more letters after de name
        (\s)            # Spece berween name and last name 
        (Nakamoto)     # Expresion n
        )''', re.VERBOSE)
    mo21 = numsRegex.findall(item)
    if mo21 != []:
        print(mo21)


# 22
print('\n','------22------','\n')
text = ['Alice eats apples.','Bob pets cats.','Carol throws baseballs.','Alice throws Apples.','BOB EATS CATS.','RoboCop eats apples.', 
        'ALICE THROWS FOOTBALLS.', 'Carol eats 7 cats.','Alice throws Apples red.','Alice throws Apples yellow and red.']
for item in text:
    numsRegex = re.compile(r'''(
        (Alice|Bob|Carol)      # Expresion n
        \s      # Expresion n
        (eats|pets|throws)
        \s
        (apples|cats|baseballs)
        \s*
        ((.*)*)
        (.)
        )''', re.VERBOSE | re.IGNORECASE)
    mo22 = numsRegex.findall(item)
    if mo22 != []:
        print(mo22)

input()