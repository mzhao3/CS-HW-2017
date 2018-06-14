"""
def square(x):
    return x**2

print square(10)
print square(5) 
print square(-2) 
"""
"""
def negate(n):
    return n * -1

print negate(5)
print negate(-15) 
print negate(0) 
"""
"""
def isBig(n):
    return n > 10000
print isBig(100) 
print isBig(10000)
print isBig(10001) 
"""
"""
def isEven(n):
    return n%2 == 0

print isEven(12)
print isEven(11)
print isEven(0) 
"""
import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
print distance(3, 0, 0, 4) 
print distance(1, 0, 2, 0)
print distance(0, 0, 8, 15)
