def isCap(c):
    return c < 'a' and c.isalpha()

def hasThreeCaps(s):
    i = 1
    value = False
    while i < len(s) - 1:
        value = isCap(s[i-1]) and isCap(s[i]) and isCap(s[i+1])
        if value == True:
            return True
        i += 1
    return value

def noConsecutiveCaps(s):
    i = 0
    value = True
    while i < len(s) - 1:
        value = not(isCap(s[i]) and isCap(s[i+1]))
        if value == False:
            return False
        i += 1
    return value

def noConsecutiveCapsSpecial(s):
    i = 1
    value = True
    while i < len(s) - 1:
        value = not(isCap(s[i]) and isCap(s[i+1]))
        if value == False:
            return False
        i += 1
    return value

def myUpper(s):
    string = ''
    i = 0
    while i < len(s):
        upper = s[i:].capitalize()
        string = string + upper[0]
        i += 1
    return string

def getSandwich(s):
    i = s.find('bread')
    print i
    j = 1
    while s.find('bread',j) > 0:
        j += 1
    print j
    return s[i+5:j -1]


## this is very wronk 
