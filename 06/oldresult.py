#!/usr/bin/python
print "Content-Type:text/html\n"

import cgitb
cgitb.enable()
import cgi
form = cgi.FieldStorage()

# ZHAO, MAGGIE
# INTRO2, PD 4
# HW 05
# 2017-05-12

if 'degrees' in form:
    degrees = forms["degrees"].value
else:
    print """<a href="lisa.stuy.edu/~mzhao3/06/Conversion(i).html"> Resubmit Form </a>"""
def dowhat():
    huh = "-1"
    if 'huh' in form:
        huh = form['huh'].value
    if huh == "+1":
        return int(degrees) + 1
    else:
        return int(degrees) - 1

#print dowhat()
TITLE= "Conversion"

BODY = str(dowhat())
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
""" + HEADER  + "Your answer is " + BODY + " degrees."+ """

</body></html>"""

print whole
