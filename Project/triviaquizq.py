#!/usr/bin/python
print 'content-type: text/html\n'
import cgi
import cgitb
import hashlib
cgitb.enable()
import random
import os
import os.path


text = open("triviaquizq.txt", "r").read()
text = text.split("\n")
for i in range(len(text)):
    text[i] = text[i].split("#")

#THIS IS A TEMPLATE TO STAY LOGGED IN BETWEEN PAGES

def mainPage(email,magicNumber):
    #note that ALL links to new pages must include this after the .py 
    cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)
    #see example below:
    print'''<!DOCTYPE= html> 
<html> 
        <link rel="stylesheet" type="text/css" href="home.css"> 
            <ul>
  		<li><a href= home.py''' + cgistuff+ '''">Home</a></li>
  		<li><a class = "active" href="quizzes.py'''+ cgistuff+ '''">Quizzes</a></li>
  		<li><a href="#info">Info</a></li>
  		<li><a href="blogpost.py'''+ cgistuff+ '''">Blog</a></li>
            </ul>
	<title> Star Wars Trivia </title> <br>
	<body> 
		<form method="GET" action="trivia.py"> 
	<input type="hidden" name="UserEmail" value="'''+email+ '''" />
        <input type="hidden" name="magicNumber" value="''' +  str(magicNumber) +'''" />
'''
    total()

def main():
    form = cgi.FieldStorage()

    #list of all required fieldstorage keys
    requiredFields = ['UserEmail','magicNumber']
    allHere = True
    for req in requiredFields:
            allHere = allHere and req in form

    #check for required fields
    if not allHere:
        print "Not logged in properly (not all form elements)."
        return

    #get the name of the data file
    email = form['UserEmail'].value
    filename = "../data/accounts/"+email+".txt"

    #check if file exists
    if not os.path.isfile(filename):
        print "Not logged in properly (bad username)."
        return

    #open file for magic number and IP
    userInfo = open(filename).read().split("\n")
    storedMagicNumber = userInfo[2]
    storedIP = userInfo[3]
    
    
    #check magic number
    magicNumber = form['magicNumber'].value
    if storedMagicNumber != magicNumber:
        print "Not logged in properly (badMagicNumber)."
        return

    #check IP address
    IP = os.environ["REMOTE_ADDR"]
    if str(IP)!=storedIP:
        print "Not logged in properly (invalid IP)."
        return                
    

    #You got here? Great! Show the real page.
    mainPage(email,magicNumber)        

def makequiz():
    for i in range(len(text)):
        z= 0
        for j in range(len(text[i])):
            if j == 0:
                print text[i][j], """<br>"""
            else:
                z+= 1
                print """<input type="radio" name='""",i + 1,"""'value = '""" ,text[i][j],"""'>""",text[i][j],""" <br>"""
def htmlclose():
    print """Answered all the questions? Submit your results here! <br>
			<input type="submit" name="submit" value="finish"> <br>

	</body> 
</html> 
"""
def total():
    makequiz()
    htmlclose()

main()
