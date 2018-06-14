def double_char(str):
    string = ""
    i = 0
    while i < len(str):
        string = string + str[i] + str [i]
        i = i + 1
    return string

def count_hi(str):
    return str.count("hi")

def cat_dog(str):
    numcat = str.count("cat")
    numdog = str.count("dog")
    return numcat == numdog

def count_code(str):
    i = 0
    count = 0
    while i < len(str) - 3:
        if str.find('co',i) == i:
            if str[i+3] == 'e':
                count = count + 1
        i = i + 1
    return count

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)

def xyz_there(str):
    #return str.count('xyz') > 0 and str.endswith('.xyz') == 0
    if str.count('.xyz') == 0:
        return str.count('xyz') > 0
    else:
        return False
def findWord(original,word):
    i = 0
    if original.count(word) > 0:
        while i < len(original) - (len(word) - 1):
            if original[i:i+len(word)] == word:
                return i
            i = i + 1
    return -1

def countWord(original,word):
    i = 0
    count = 0
    if original.find(word) > -1:
        while i < len(original):
            if original[i:i+ len(word)] == word:
                count = count + 1
            i = i + 1
    return count
