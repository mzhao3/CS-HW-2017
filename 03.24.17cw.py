def makeSentence(L):
    i = 0
    string = ''
    while i < len(L):
        string = string + ' ' + L[i]
        i += 1
    return string[1:]

def makeFibList(n):
    i = 1
    fiblist = [0, 1]
    while i < n:
        fiblist.append(fiblist[i-1] + fiblist[i])
        i += 1
    return fiblist[:n+1]

def fib(n):
    return makeFibList(n)[n]

