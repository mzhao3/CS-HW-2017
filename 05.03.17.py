def tally(L):
    d = {}
    for i in range(len(L)):
        if L[i] in d:
            d[L[i]] = d[L[i]] + 1
        else:
            d[L[i]] = 1
    print d
"""
def tally2(L):
    d = {}
    for i in range(len(L)):
        if L[i].isalpha():
            if L[i].lower() in d:
                d[L[i].lower()] = d[L[i].lower()] + 1
            else:
                d[L[i].lower()] = 1
        else:
            if L[i] in d:
                d[L[i]] = d[L[i]] + 1
            else:
                d[L[i]] = 1
    print d
    """
def tally2(L):
    d = {}
    for i in range(len(L)):
        if L[i].lower() in d:
             d[L[i].lower()] = d[L[i].lower()] + 1
        else:
             d[L[i].lower()] = 1
    
    print d
