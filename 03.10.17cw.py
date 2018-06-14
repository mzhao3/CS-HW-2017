def bunnyEars(n):
    if n== 0:
        return 0
    else:
        return 2 + bunnyEars(n-1)

def what(s):
    if len(s) < 2:
        return 0
    else:
        if s[:2] == 'hi':
            return 1 + what(s[1:])
        else:
            return what(s[1:])
