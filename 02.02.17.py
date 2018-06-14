#makes10
def makes10(a, b):
    return a + b == 10 or a == 10 or b == 10
    
print makes10(9, 10) 
print makes10(9, 9) 
print makes10(1, 9)

#sleep_In
def sleep_in(weekday,vacation):
    return not weekday or vacation

print sleep_in(False, False) 
print sleep_in(True, False) 
print sleep_in(False, True) 

#monkey_trouble
def monkey_trouble(a_smile,b_smile):
    return (a_smile and b_smile) or (not a_smile and not b_smile)

print monkey_trouble(True, True)
print monkey_trouble(False, False) 
print monkey_trouble(True, False) 
