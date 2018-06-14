# pos_neg
def pos_neg(a, b, negative):
    if negative == False:
        return a * b < 0
    else:
        return a < 0 and b < 0
print pos_neg(1, -1, False) 
print pos_neg(-1, 1, False) 
print pos_neg(-4, -5, True) 

# sorta_sum
def sorta_sum(a,b):
    if a + b > 9 and a + b < 20:
        return 20
    else:
        return a + b
print sorta_sum(3, 4)
print sorta_sum(9, 4)
print sorta_sum(10, 11)

# near_ten
def near_ten(num):
    return num % 10 >= 8 or num % 10 <= 2
print near_ten(12)
print near_ten(17) 
print near_ten(19)

# love6
def love6(a,b):
    return a==6 or b==6 or a+b==6 or abs(a-b)==6

print love6(6, 4) 
print love6(4, 5) 
print love6(1, 5) 

# lone_sum
def lone_sum(a,b,c):
    if a == b and b == c: 
        return 0
    elif a == b:
        return c
    elif b == c:
        return a
    elif a == c:
        return b
    else:
        return a + b + c
print lone_sum(1, 2, 3) 
print lone_sum(3, 2, 3)
print lone_sum(3, 3, 2)
print lone_sum(2, 3, 3) 
print lone_sum(3, 3, 3)

# lucky_sum
def lucky_sum(a, b, c):
    if a== 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c
print lucky_sum(1, 2, 3) 
print lucky_sum(1, 2, 13) 
print lucky_sum(1, 13, 3)

# fix_teen and no_teen_sum
def fix_teen(n):
    if n == 15 or n == 16:
        return n
    if n > 12 and n < 20:
        return 0
    else:
        return n

print fix_teen(15)
print fix_teen(20)
print fix_teen(12)
print fix_teen(17)

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
print no_teen_sum(1, 2, 3) 
print no_teen_sum(2, 13, 1)
print no_teen_sum(2, 1, 14) 


