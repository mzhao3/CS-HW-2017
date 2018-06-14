#!/usr/bin/python
print 'content-type: text/html\n'
import cgi
import cgitb
cgitb.enable()
form=cgi.FieldStorage()
#print form
i=1
numcorrect=0
numtotal=0#loops through each group radio box on the form
while 'group'+str(i) in form:#this only works if you fill out every question
    numtotal += 1#you always add 1 to the total number of test questions
    answ=form.getvalue('group'+str(i))
    if answ=='correct':
        numcorrect+=1#evry time you get a correct answer adds one to numcorrect
    i += 1
#print (numcorrect//numtotal)
print (numcorrect)
print ' questions correct out of '
print (numtotal)
print 'questions'
