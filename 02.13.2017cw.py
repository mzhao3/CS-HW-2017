
def printHail(n):
    while n > 1:
        if n%2 == 0:
            print n,
            n = n / 2
        else:
            print n,
            n = 3 * n + 1
    print 1 
"""       
printHail(1)
printHail(2)
printHail(3)
printHail(4)
printHail(5)
printHail(6)
printHail(9)
"""
def hailLen(n):
    output = 1
    while n > 1:
        if n%2 == 0:
            output = output + 1
            n = n / 2
        else:
            output = output + 1
            n = 3 * n + 1
    return output
"""        
print hailLen(1)
print hailLen(2)
print hailLen(3)
print hailLen(4)
print hailLen(5)
print hailLen(6)
print hailLen(9)
"""
def maxHail(z):
    i = 0
    length1 = 0
    while i < z:
        i = i + 1
        length2 = hailLen(i) 
        if length2 > length1:
            length1 = length2
            maxx  = i
    return maxx
print maxHail(1)
print maxHail(2)
print maxHail(3)
print maxHail(4)
print maxHail(5)
print maxHail(6)

