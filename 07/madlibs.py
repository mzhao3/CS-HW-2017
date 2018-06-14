#!/usr/bin/python
print "Content-Type:text/html\n"

import cgitb
cgitb.enable()
import cgi
form = cgi.FieldStorage()

# ZHAO, MAGGIE
# INTRO2, PD 4
# HW 07
# 2017-05-20

text = open("story.txt", "r").read()
text= text.replace("--", " ")
text = text.split()

# Remove punctuation
for i in range(len(text)):
    text[i] = text[i].strip("""",.\/;:!?[]{}()_'@#%^&*|~`""")

lists = {"$person1$","$person2$","$adjective1$", "$adjective2$", "$adjective3$", "$number1$", "$number2$", "$-ing-verb1$", "$-ing-verb2$", "$-ing-verb3$", "$past-tense-verb1$", "$past-tense-verb2$", "$past-tense-verb3$"}
special = {"$person1$'s"}
def replacement(t):
    for i in range(len(t)):
        if t[i] in lists:
            t[i]= form[t[i]].value
        elif t[i] in special:
            t[i]= form["$person1$"].value + "\'s"
    return t
finaltext = (replacement(text))

finaltext = ' '.join(finaltext)


TITLE= "Your MadLibs Result!" 
BODY = finaltext
HEADER = """
# ZHAO, MAGGIE<br>
# INTRO2, PD 4<br>
# HW 07<br>
# 2017-05-20<br>
"""
whole = """<!DOCTYPE html>
<html>
<head><title>"""+TITLE +"""</title></head>
<body>
""" + HEADER  + BODY + """ <br> </body></html>"""

print whole

