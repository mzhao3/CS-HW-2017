#!/usr/bin/python
print "Content-Type:text/html\n"

# ZHAO, MAGGIE
# INTRO2, PD 4
# HW 05
# 2017-05-12

import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

degree = int(form.getvalue("degrees"))
huh = form.getvalue("huh")

def tocelsius(degrees):
    return str(float ((degree - 32.0) * (5.0/9.0)))

def tofahrenheit(degrees):
    return str(float(degree * (9.0/5.0) - 32.0))

"""
def makebody():
    if 'degrees' in form:
        dowhat()
    else:
        BODY = "<a href="lisa.stuy.edu/~mzhao3/06/form.html"> Resubmit Form </a>"
"""
def dowhat():
    if huh == "Fahrenheit":
        print "Your answer is " + tocelsius(degree) + " degrees Celsius."
    if huh == "Celsius":
        print "Your answer is " + tofahrenheit(degree) + " degrees Fahrenheit."

dowhat()
