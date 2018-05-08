import re
password = input()
# password = 'password'
def strongPasswordDetector(password):
    strongPasswordLength = re.compile(r'\w{8,}')
    mo1 = strongPasswordLength.search(password)
    # if mo == None:
    #     print('Bad password - Length')
    #     return False

    strongPasswordUpper = re.compile(r'[A-Z]')
    mo2 = strongPasswordUpper.search(password)
    # if mo2 == None:
    #     print('Bad password - Upper')
    #     return False
    
    strongPasswordLower = re.compile(r'[a-z]')
    mo3 = strongPasswordLower.search(password)
    # if mo3 == None:
    #     print('Bad password - Lower')
    #     return False

    strongPasswordNum = re.compile(r'\d')
    mo4 = strongPasswordNum.search(password)
    # if mo4 == None:
    #     print('Bad password - Num')
    #     return False

    if (mo1 != None) and (mo2 != None) and (mo3 != None) and (mo4 != None):
        print('Good password')
        return True
    else:
        print('Bad Password in general')
        return False

        

strongPasswordDetector(password)
input()