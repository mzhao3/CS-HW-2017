
def fact(n):
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)


    
def exp(b,e):
    if e < 0:
        return 1.0/b * exp(b,e+1)
        # return 1.0/exp(b, -e)
    elif e == 0:
        return 1
    else:
        return b * exp(b,e-1)
