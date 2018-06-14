def isCap(c):
    return c < 'a' and c.isalpha()
def myCapitalize(s):
    i = 0
    string = ''
    while i < len(s):
        if i == 0:
            string = string + s[i].upper()
        else:
            string = string + s[i].lower()
        i = i + 1
    return string           
def maxHailRange(low,high):
  i = low
  length1 = 0
  while i <= high:
    length2 = hailLen(i) 
    if length2 > length1:
      length1 = length2
      maxx  = i
    i = i + 1
  return maxx  
def hailLen(z):
    output = 1
    while z > 1:
        if z%2 == 0:
            output = output + 1
            z = z / 2
        else:
            output = output + 1
            z = 3 * z + 1
    return output  
def specialSumInclusive(n):
  x = 0
  sumx = 0
  while x <= n:
    if x%5 == 0 or x%3 == 0:
      sumx = sumx + x
    x = x + 1
  return sumx

def getSandwich(s):
  string = ''
  numb= s.count("bread")
  if numb > 2 :
    i = s.find("bread")
    j = s.find("bread",(numb - 1) * 5 )
    string = s[i + 5 : j]
  return string  
