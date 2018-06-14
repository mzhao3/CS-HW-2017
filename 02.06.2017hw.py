'''
def diff21(n):
    diff = abs ( n - 21)
    if n <= 21:
        return diff
    else:
        return 2 * diff

print diff21(19) 
print diff21(10) 
print diff21(21)
'''
'''
def parrot_trouble(talking, hour):
    return talking and ( hour < 7 or hour > 20 )

print parrot_trouble(True, 6) 
print parrot_trouble(True, 7) 
print parrot_trouble(False, 6) 
'''
def near_hundred(n):
    return abs ( n- 100) <= 10 or abs (n-200) <= 10
print near_hundred(93) 
print near_hundred(90) 
print near_hundred(89)
print near_hundred(189)
print near_hundred(199)
print near_hundred(201)
print near_hundred(301)
print near_hundred(50) 
