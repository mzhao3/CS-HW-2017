#!/usr/bin/python
print "Content-Type:text/html\n"

# ZHAO, MAGGIE
# INTRO2, PD 4
# HW 05
# 2017-05-07

#FUNCTIONS

def tally(L):
    d = {}
    for i in range(len(L)):
        if L[i].lower() in d:
             d[L[i].lower()] = d[L[i].lower()] + 1
        else:
             d[L[i].lower()] = 1
    return d

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


text = open("WotW.txt", "r").read()


text= text.replace("--", " ")
ONE = text.split()

for i in range(len(ONE)):
    ONE[i] = ONE[i].strip('[],.!?;:"{}()_')
    ONE[i] = ONE[i].strip("',")
ONE = filter(None, ONE)
totalwords = len(ONE)
unique = tally(ONE)
ONE = sorted(unique.keys())

heading = ["ID", "Word", "count"]

listofthings = []
i = 0
for i in range(len(ONE)):
    listofthings.append([i, ONE[i], unique[ONE[i]]])
    i += 1
character = 0
for i in range(len(ONE)):
    character = character + len(ONE[i])
over250 = 0
for key in unique:
    if unique[key] > 250:
        over250 += 1
usedonce = 0
for key in unique:
    if unique[key] == 1:
        usedonce+= 1
over15 = 0
longwords = ""
for key in unique:
    if len(key) > 15:
        over15 += 1
        longwords = longwords + key +" "
longwords = longwords.split()
longwords = sorted(longwords)
STAT = str(len(open("waroftheworlds.txt", "r").read())) + " characters in the text file. <br>" + str(totalwords) + " words in the book. <br>" +str(len(unique)) + " unique words in the book. <br>" + str(over250) + " words that are used over 250 times. <br>" +str(usedonce) + " words that are used once. <br>" + str(over15) + " words that are over 15 letters long. <br>"

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

""" + HEADER + STAT + str(longwords) + str(ONE)+ BODY + """

</body></html>"""

#print whole

