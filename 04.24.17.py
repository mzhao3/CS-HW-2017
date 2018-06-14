def removeValuesFromXtoYList(l,x,y):
    i = 0
    while i < len(l):
        if x < l[i] < y:
            l.pop(i)
            i = i-1
        i += 1

def moveNegativeToEnd(x):
    i = 0
    Neg = []
    while i< len(x):
        if x[i] < 0:
            Neg.append(x[i])
            x.pop(i)
            i += -1
        i += 1
    z =0
    while z < len(Neg):
        x.append(Neg[z])
        z+=1
"""
x=[ 1, 3, -5, 10, -2, 0, -6.0]
moveNegativeToEnd(x)  
print x

y=[0, 1 , -3, 4.5]
moveNegativeToEnd(y) 
print y
"""
def reverseWordsWithCapitals(L):
    i = 0
    while i<len(L):
        if not L[i].islower():
            L[i] = L[i][::-1]
        i += 1

x = ['fish','Hey!','oOps','this is Sparta!']
reverseWordsWithCapitals( x ) 
print x 
        

