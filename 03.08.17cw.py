def valueOF(c):
    return (ord(s[i]) - ord('0'))
    #return '0123456789'.find(c)
def myInt(s):
    i = -1
    exp = 0
    sumnum = 0
    while abs(i) <= len(s):
        sumnum = sumnum + (ord(s[i]) - ord('0'))* (10**exp)
        print sumnum
        exp += 1
        i += -1
    return sumnum

def myInt2(s):
    if s[0] == '-':
        i = 1
    else:
        i = 0
    sumnum = 0
    while i < len(s):
        sumnum = sumnum * 10 + (ord(s[i]) - ord('0'))
        i += 1                                
    if s[0] != '-':
        return sumnum
    else:
        return sumnum * -1
