"""
def sumOfPowers(n):
    power = 1
    sumpower= 0
    while 2**power <= n:
        sumpower = sumpower + 2 ** power
        power = power + 1
    return sumpower

print sumOfPowers(0) 
print sumOfPowers(10) 
print sumOfPowers(2) 
"""
        
def sumAtoB(a,b):
    sumab = 0
    while a <= b:
        sumab = sumab + a
        a = a + 1
    return sumab
"""
print sumAtoB(0, 1) 
print sumAtoB(1, 3) 
print sumAtoB(2, 0)
"""
def sumRange(a,b):
    if a < b:
        return sumAtoB(a,b)
    else:
        return sumAtoB(b,a)

print sumRange(1, 2) 
print sumRange(2, 1) 
print sumRange(-3, -10)
