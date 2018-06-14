def isVowel(letter):
    letter= letter.lower()
    A = letter == 'a'
    E = letter == 'e'
    I = letter == 'i'
    O = letter == 'o'
    U = letter == 'u'
    return A or E or I or O or U
def noVowels(s):
    i = 0
    result = ""
    while i < len(s):
        if not isVowel(s[i]):
            result = result + s[i]
        i = i + 1
    return result
