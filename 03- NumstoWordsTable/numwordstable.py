# ZHAO, MAGGIE 
# INTRO2, PD 4 
# HW 03
# 2017-05-01

##Functions
def numToWordsLarge(n):
    singleslist = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tenslist = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n < 100:
        if n < 20:
            return singleslist[n]
        elif n % 10 != 0:
            return tenslist[n/10-2] + "-" + numToWordsLarge(n%10)
        elif n%10 == 0:
            return tenslist[n/10-2]
    elif n < 1000:
        if n %100 != 0:
            return numToWordsLarge(n/100) + " hundred and " + numToWordsLarge(n%100)
        else:
            return numToWordsLarge(n/100) + " hundred"
    elif n < 1000000:
        if n % 1000 != 0:
            return numToWordsLarge(n/1000) + " thousand " + numToWordsLarge(n%1000)
        else:
            return numToWordsLarge(n/1000) + " thousand"

def makeTag(d, tag):
    return "<" + tag + ">" + str(d) + "</" + tag + ">"

def makeRow(row, tag):
    final = "<tr>"
    for i in range(len(row)):
        final = final + makeTag(row[i], tag)
    final = final + "</tr>"
    return final

def toHTMLTable(header, L):
    table =  "<table>" + "\n"
    table = table + makeRow(header, "th") + "\n"
    for row in L:
        table = table + makeRow(row,"td") + "\n"
    table = table + "</table>"
    return table

listofthings = []
for i in range(0, 1235):
    listofthings.append([i, numToWordsLarge(i)])
    
header = ["Number", "Words"]
TITLE= "NumtoWordsTable"
BODY = toHTMLTable(header, listofthings)
HEADER = """# ZHAO, MAGGIE <br>
# INTRO2, PD 4 <br>
# HW 03 <br>
# 2017-05-01 <br> """
whole = """<!DOCTYPE html>
<html>
<head><title>"""+TITLE +"""</title></head>
<body>

""" + HEADER + BODY + """

</body></html>"""

print whole
