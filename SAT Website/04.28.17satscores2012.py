# ZHAO, MAGGIE
# INTRO2, PD 4
# HW --
# 2017-04-29

file = open("SAT_Results.csv", "r")
data2012 = file.read().split("\n")
for i in range(len(data2012)):
    data2012[i] = data2012[i].split(",")

for row in data2012:
    row[5] = row[5][:-1]
header2012 = data2012.pop(0)

def totalscore(row):
    sumnums = 0
    for element in row[3:]:
        if element.isalpha():
            sumnums = "s"
        if not element.isalpha():
            element = float(element)
            sumnums = sumnums + element
    return sumnums

for row in data2012:
    row.append(totalscore(row))

header2012.append("Total Score")

def makeTag(d, tag):
    return "<" + tag + ">" + str(d) + "</" + tag + ">"

def makeRow(row, tag):
    final = "<tr>"
    for i in range(len(row)):
        final = final + makeTag(row[i], tag)
    final = final + "</tr>"
    return final

def toHTMLTable(L):
    table =  "<table>" + "\n"
    table = table + makeRow(header2012, "th") + "\n"
    for row in L:
        table = table + makeRow(row,"td") + "\n"
    table = table + "</table>"
    return table
 
TITLE= "SAT 2012"
BODY = toHTMLTable(data2012)
HEADER = """# ZHAO, MAGGIE <br>
# INTRO2, PD 4 <br>
# HW -- <br>
# 2017-04-29 <br>
"""
whole = """<!DOCTYPE html>
<html>
<head><title>"""+TITLE +"""</title></head>
<body>

""" + HEADER + BODY + """

</body></html>"""

print whole
