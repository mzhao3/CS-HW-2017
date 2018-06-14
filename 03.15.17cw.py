def gcfRec(a,b):
    if a % b == 0:
        return b
    else:
        remain = a % b
        a = b
        b = remain
        return gcfRec(a,b)

def gcfLoop(a,b):
    while a % b != 0:
        remain = a % b
        a = b
        b = remain
    return b

print gcfRec(225,243)
print gcfLoop(225,243)
