import re
# 20
text = ['1,23','42','1,234','6,368,745','12,34,567','1234']
for item in text:
    numsRegex = re.compile(r'''(
        (^\d{1,3})      # Expresion n
        (,\d{3})*$      # Expresion n
        )''', re.VERBOSE)
    mo20 = numsRegex.findall(item)
    print(mo20)

# 21
text = ['Satosh Nakamoto','Alice Nakamoto','RoboCop Nakamoto','satoshi Nakamoto','Mr. Nakamoto','Nakamoto', 'Satoshi nakamoto']
for item in text:
    numsRegex = re.compile(r'''(
        (^\d{1,3})      # Expresion n
        (,\d{3})*$      # Expresion n
        )''', re.VERBOSE)
    mo21 = numsRegex.findall(item)
    print(mo21)


# 22
text = ['Alice eats apples.','Bob pets cats.','Carol throws baseballs.','Alice throws Apples.','BOB EATS CATS.','RoboCop eats apples.', 'ALICE THROWS FOOTBALLS.', 'Carol eats 7 cats.']
for item in text:
    numsRegex = re.compile(r'''(
        (^\d{1,3})      # Expresion n
        (,\d{3})*$      # Expresion n
        )''', re.VERBOSE)
    mo22 = numsRegex.findall(item)
    print(mo22)


input()