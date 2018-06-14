#!/usr/bin/python
print "Content-Type:text/html\n"
import cgitb
cgitb.enable()

# ZHAO, MAGGIE
# INTRO2, PD 4
# HW 05
# 2017-05-07

#FUNCTIONS

    # creates a dictionary of all words
def tally(L):
    d = {}
    for i in range(len(L)):
        if L[i].lower() in d:
             d[L[i].lower()] = d[L[i].lower()] + 1
        else:
             d[L[i].lower()] = 1
    return d
	
    # makes tags for each table cell
def makeTag(d, tag):
    return "<" + tag + ">" + str(d) + "</" + tag + ">"

    # makes rows for the table
def makeRow(row, tag):
    final = "<tr>"
    for i in range(len(row)):
        final = final + makeTag(row[i], tag)
    final = final + "</tr>"
    return final

    # final table, given a header and a data list
def toHTMLTable(header, L):
    table =  "<table>" + "\n"
    table = table + makeRow(header, "th") + "\n"
    for row in L:
        table = table + makeRow(row,"td") + "\n"
    table = table + "</table>"
    return table

    # uses data from URL
import cgi
formdata= cgi.FieldStorage()
    # default book
name = "WotW"
if 'name' in formdata:
    name = formdata['name'].value
#import random
#names= ["WotW","Frank","holmes"]
#used = random.choice(names)
    # Open text, replace "--" with " ", and split 
text = open(name +".txt", "r").read()
text= text.replace("--", " ")
ONE = text.split()
    # Get rid of all punctuation
for i in range(len(ONE)):
    ONE[i] = ONE[i].strip('[],.!?;:"{}()_')
    ONE[i] = ONE[i].strip("',.!?")
    # Gets rid of empty strings
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
    # Number of words used over 250 times	
over250 = 0
for key in unique:
    if unique[key] > 250:
        over250 += 1
    # Number of words used once
usedonce = 0
for key in unique:
    if unique[key] == 1:
        usedonce+= 1
    # Number of words with length over 15 are counted and added to a list
over15 = 0
longwords = ""
for key in unique:
    if len(key) > 15:
        over15 += 1
        longwords = longwords + key +" "
longwords = longwords.split()
longwords = sorted(longwords)
STAT = str(len(open(name+".txt", "r").read())) + " characters in the text file. <br>" + str(totalwords) + " words in the book. (total, not unique) <br>" +str(len(unique)) + " unique words in the book. (all words converted to lowercase) <br>" + str(over250) + " words that are used over 250 times. <br>" +str(usedonce) + " words that are used once. <br>" + str(over15) + " words that are over 15 letters long. <br>"

title = {"WotW":"War of the Worlds", "holmes":"Sherlock Holmes","Frank":"Frankenstein"}
TITLE= title[name]

BODY = toHTMLTable(heading, listofthings)
HEADER = """
# ZHAO, MAGGIE<br>
# INTRO2, PD 4<br>
# HW 05<br>
# 2017-05-07<br>
<h3> Other Links! </h3>
<a href="lisa.stuy.edu/~mzhao3/05/wordcountCGI.py?name=WotW">View War of the Worlds</a>
<a href="lisa.stuy.edu/~mzhao3/05/wordcountCGI.py?name=Frank">View Frankenstein</a>
<a href="lisa.stuy.edu/~mzhao3/05/wordcountCGI.py?name=holmes">View Sherlock Holmes</a>


"""
whole = """<!DOCTYPE html>
<html>
<head><title>"""+TITLE +"""</title></head>
<body>

""" + HEADER + "<h1>" + TITLE + "</h1>" + STAT + "<h3> Long words </h3> " + str(longwords) + "<h3> Unique words </h3> " +str(ONE)+ "<h3> Words occuring more than 0 times</h3> " +  BODY + """

</body></html>"""

print whole


