def removeCharFromString(s,c):
    i = 0
    string =''
    while i < len(s):
        if s[i] != c:
            string = string + s[i]
        i += 1
    return string 

def removeFromString(s,part):
    i = 0
    string = ''
    while i + len(part) < len(s) + len(part):
        if s[i:len(part)+i] != part:
            string = string+ s[i]
            i += 1
        else:
            i = i + len(part)
    return string 
        
def makeBoxOfNumbers(rows,cols):
    i = 0
    string = ''
    while i < rows * cols:
        string = string + str(i%10)
        i += 1
        if i %cols == 0:
            string = string + '\n'
    print string
