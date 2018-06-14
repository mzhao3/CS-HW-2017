def ones_digit(n):
    return n % 10
def tens_digit(n):
    return (n % 100 - ones_digit (n)) / 10
#    return ((( n - ones_digit(n)) / 10 ) % 10

def magicValue(n):
    if ones_digit(n) != tens_digit(n):
        return ones_digit(n) +  tens_digit(n)
    else:
        return ones_digit(n)

print magicValue(2)
print magicValue(118)
print magicValue(188)
print magicValue(123)
print magicValue(111)
print magicValue(10)
print magicValue(99999999999999)
print magicValue(9923456)
