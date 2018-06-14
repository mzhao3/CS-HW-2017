def makeEvenListToN(n):
    i = 0
    l = []
    while 2*i <= n:
        l.append(2*i)
        i+= 1
    return l

def makeListOneToN(n):
    i= 1
    l = []
    while i <= n:
        l.append(i)
        i+= 1
    return l

def makeSentence(L):
    string = ""
    i = 0
    while i < len(L):
        string = string + " " + L[i]
        i += 1
    return string[1:]
