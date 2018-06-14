"""
def sumFromZeroToN(n):
    if n >= 0:
        sumn = 0
        x = 0
        while x < n:
            x = x + 1
            sumn = sumn + x
        return sumn
    else:
        return 0
print sumFromZeroToN(-3) 
print sumFromZeroToN(4) 
print sumFromZeroToN(10)     
"""
"""
def fiveSumFromZeroToN(n):
    if n >= 0:
        x = 0
        sumx = 0
        while x <= n:
            x5 = x % 5
            if x5 == 0:
                sumx = sumx + x
            x = x + 1
        return sumx
    else:
        return 0

print fiveSumFromZeroToN(0) 
print fiveSumFromZeroToN(10) 
print fiveSumFromZeroToN(33)
"""
"""
def specialSum(n):
    x = 0
    sumx = 0
    while x <= n:
        if x%35 == 0:
            sumx = sumx + x
        x = x + 1
    return sumx
    
print specialSum(5) 
print specialSum(7) 
print specialSum(35)
"""
def sumSquares(n):
    if n >= 0:
        a = 0
        sumsquare= 0
        while a <= n:
            sumsquare = sumsquare + a**2
            a = a + 1
        return sumsquare
    else:
        return 0
print sumSquares(1) 
print sumSquares(2) 
print sumSquares(3)
