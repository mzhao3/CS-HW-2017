# ZHAO, MAGGIE
# INTRO2, PD 4
# HW --
# 2017-04-29

file = open("SAT__College_Board__2010_School_Level_Results.csv", "r")
data2010 = file.read().split("\n")
for i in range(len(data2010)):
    data2010[i] = data2010[i].split(",")

for row in data2010:
    row[5] = row[5][:-1]
header2010 = data2010.pop(0)

def totalscore(row):
    sumnums = 0
    for element in row[3:]:
        if element.isalpha():
            sumnums = "s"
        if not element.isalpha():
            element = float(element)
            sumnums = sumnums + element
    return sumnums

for row in data2010:
    row.append(totalscore(row))

header2010.append("Total Score")

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
 
TITLE2010= "SAT 2010"
BODY2010 = toHTMLTable(header2010,data2010)
HEADER = """# ZHAO, MAGGIE<br>
# INTRO2, PD 4<br>
# HW --<br>
# 2017-04-29<br>"""
whole2010 = """<!DOCTYPE html>
<html>
<head><title>"""+TITLE2010 +"""</title></head>
<body>

""" + HEADER + BODY2010 + """

</body></html>"""

print whole2010
