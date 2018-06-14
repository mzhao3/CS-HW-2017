# ZHAO, MAGGIE
# INTRO2, PD 4
# HW 05
# 2017-05-07

text = open("waroftheworlds.txt", "r").read()
text = text[:4112]

text= text.replace("--", " ")
ONE = text.split()

for i in range(len(ONE)):
    ONE[i] = ONE[i].strip('[],.!?;:"{}()_')
    ONE[i] = ONE[i].strip("'")
ONE = filter(None, ONE)
#print ONE
#5ai)
character = 0
for i in range(len(ONE)):
    character = character + len(ONE[i])
print character    
#5aii)
print len(ONE)
#5aiii)
def tally(L):
    d = {}
    for i in range(len(L)):
        if L[i].lower() in d:
             d[L[i].lower()] = d[L[i].lower()] + 1
        else:
             d[L[i].lower()] = 1
    return d

unique = tally(ONE)

unique1 = sorted(unique.items())
ONE = sorted(unique.keys())
print len(unique)
#5aiv
over20 = 0
for key in unique:
    if unique[key] > 20:
        over20 += 1
print over20
#5av
usedonce = 0
for key in unique:
    if unique[key] == 1:
        usedonce+= 1
print usedonce
#5avi
over12 = 0
for key in unique:
    if len(key) > 12:
        over12 += 1
print over12

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
heading = ["ID", "Word", "count"]


listofthings = []
i = 0
for i in range(len(ONE)):
    listofthings.append([i, ONE[i], unique[ONE[i]]])
    i += 1

TITLE= "Word Count"
BODY = toHTMLTable(heading, listofthings)
HEADER = """
# ZHAO, MAGGIE<br>
# INTRO2, PD 4<br>
# HW 05<br>
# 2017-05-07<br>
"""
whole = """<!DOCTYPE html>
<html>
<head><title>"""+TITLE +"""</title></head>
<body>

""" + HEADER + BODY + """

</body></html>"""

print whole



