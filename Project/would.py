#!/usr/bin/python
print 'content-type: text/html\n'
import cgi
import cgitb
import hashlib
cgitb.enable()
import random
import os
import os.path


def mainPage(email,magicNumber):
    #note that ALL links to new pages must include this after the .py 
    cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)
    print """<!DOCTYPE=html> <br>
            <html> <br>
            <head> <br>
            <link rel="stylesheet" type="text/css" href="home.css"> <br>
            <ul>
  		<li><a href= home.py""" + cgistuff+ """">Home</a></li>
  		<li><a class = "active" href="quizzes.py"""+ cgistuff+ """">Quizzes</a></li>
  		<li><a href="#info">Info</a></li>
  		<li><a href="blogpost.py"""+ cgistuff+ """">Blog</a></li>
            </ul>
            <title> Which Star Wars Character are You?! </title> <br>
            </head> <br>
            <body> <br>
            <form method="Get" action="would.py"
            <input type="hidden" name="UserEmail" size="25" value="'''+email+'''">
            <input type="hidden" name="magicNumber" size="25" value="'''+str(magicNumber)+'''">
            """
        
    choices()
    print """Answered all the questions? Submit your results here! <br>
			<input type="submit" name="submit" value="finish"> <br>
            </body> <br>
            </html> <br>
            """
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
    print mainPage(email,magicNumber)            
main()

def choices():
    form = cgi.FieldStorage()
    questions = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] #etc...
    allHere= True
    for answers in questions:
        allHere = allHere and answers in form

    #Check if all questions have been filled out.
    if not allHere:
        print "Not all questions have been answered."
    return
    choice1, choice2, choice3, choice4 = 0,0,0,0
    for answers in questions:
        if form[questions].value == 1:
            choice1 += 1
        elif form[questions].value == 2:
            choice2 += 1
        elif form[questions].value == 3:
            choice3 += 1
        elif form[questions].value == 4:
            choice4 += 1
            
    name = max(choice1, choice2, choice3, choice4)
    text = open(name + ".txt", "r")
    return text

