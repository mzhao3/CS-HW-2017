def pigLatinSimple(word):
    if word[0] in "aeiou":
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"

def pigLatinBest(word):
    if word[0] in ['a','e','i','o','u']:
        if word.isalnum():
            return word + "hay"
        else:
            return word[:-1] + "hay" + word[-1]
    elif word[0:2] in ['bl', 'br', 'ch', 'ck', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 'gl', 'gr', 'ng', 'ph', 'pl', 'pr', 'qu', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']:
        if word.isalnum():
            return word[2:] + word[0:2] + "ay"
        else:
            return word[2:-1] + word[0:2] + "ay" + word[-1]
    else:
        if word.isalnum():
            return word[1:-1] + word[0] + "ay"
        else:
            return word[1:-1] + word[0] + "ay" + word[-1]

def pigLatin(word):
    if word[0] in ['a','e','i','o','u']:
        return word + "hay"
    elif word[0:2] in ['bl', 'br', 'ch', 'ck', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 'gl', 'gr', 'ng', 'ph', 'pl', 'pr', 'qu', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']:
        return word[2:] + word[0:2] + "ay"
    else:
        return word[1:] + word[0] + "ay"
  
def capitalizeSentence(s):
    L = s.split(" ")
    i = 0
    while i < len(L):
        L[i] = L[i].capitalize()
        i += 1
    return " ".join(L)
        
def pigLatinMultiple(s):
    L = s.split()
    i = 0
    while i < len(L):
        L[i] = pigLatin(L[i])
        i += 1
    return " ".join(L)
