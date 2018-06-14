# ZHAO, MAGGIE
# INTRO2, PD 4
# HW 04
# 2017-05-02

def makeStars(rows,cols):
    starstring = ""
    for i in range(rows):
        for i in range(cols):
               starstring = starstring + "*"
        starstring = starstring + "\n"
    return starstring

def makeNums(rows, cols):
    outer = []
    inner = []
    counter = 0 
    for i in range(rows):
        for j in range(cols):
            inner.append(counter)
            counter += 1
        outer.append(inner)
        inner = []
    return outer
def makeTag(d, tag):
    return "<" + tag + ">" + str(d) + ":" + chr(d) + "</" + tag + ">"

def makeRow(row, tag):
    final = "<tr>"
    for i in range(len(row)):
        final = final + makeTag(row [i], tag)
    final = final + "</tr>"
    return final            
def makeAsciiTable():
    table =  "<table>" + "\n"
    outer = []
    inner = []
    counter = 15
    for i in range(7):
        for j in range(16):
            inner.append(counter)
            counter += 1
        outer.append(inner)
        inner = []
    print outer
    for row in outer:
        table = table + makeRow(row,"td") + "\n"
    table = table + "</table>"
    return table


TITLE= "ASCII Table"
BODY = makeAsciiTable()
HEADER = """# ZHAO, MAGGIE<br>
# INTRO2, PD 4<br>
# HW 04<br>
# 2017-05-02<br>"""
whole = """<!DOCTYPE html>
<html lang="en-US">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<head><title>"""+TITLE +"""</title></head>
<body>

""" + HEADER + BODY+ """

</body></html>"""
print whole
