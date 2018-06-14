def rot13Char(c):
    i = 0
    if c.isalpha():
        while i < 13:
            if c == 'Z':
                c = chr(ord('A') - 1)
            if c == 'z':
                c = chr(ord('a') - 1)
            c = chr(ord(c) + 1)
            i += 1
    return c

def rot13Char2(c):
    if c >= 'a' and c <= 'm' or c >= 'A' and c<= 'M':
        return chr(ord(c)+13)
    if c >= 'n' and c <= 'z' or c >= 'N' and c<= 'Z':
        return chr(ord(c)-13)
## MR K's IN-CLASS

def rot13Char3(c):
    if c.isalpha():
        if c >= 'a' and c <= 'z':
            offset = ord('a')
        if c >= 'A' and c <= 'Z':
            offset = ord('A')
        return (ord(c)-offset + 13) % 26 + offset
    return c

def rot13(s):
    b = 0
    string = ''
    while b <len(s):
        string = string + rot13Char(s[b])
        b += 1
    return string

def rotXChar(c,n):
    i = 0
    if c.isalpha():
        while i < n%26:
            if c == 'Z':
                c= chr(ord('A') - 1)
            if c == 'z':
                c = chr(ord('a') - 1)
            c = chr (ord (c) + 1)
            i += 1
    return c

def rotXChar2(c,n):
    if c.isalpha():
        if c >= 'a' and c <= 'z':
            offset = ord('a')
        if c >= 'A' and c <= 'Z':
            offset = ord('A')
        return (ord(c)-offset + n) % 26 + offset
    return c

def rotX(s,x):
    b= 0
    string = ''
    while b< len(s):
        string = string + rotXChar(s[b],x)
        b += 1
    return string
