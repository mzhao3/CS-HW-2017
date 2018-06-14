def makeEvenList(n):
    x = []
    i = 0
    while i < n:
        x.append(i*2)
        i += 1
    return x

def makeHailList(n):
    x = []
    while n > 1:
        if n%2 == 0:
            x.append(n)
            n = n / 2
        else:
            x.append(n)
            n = 3 * n + 1
    x.append(1)
    return x

