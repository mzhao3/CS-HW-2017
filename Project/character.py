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
    print'''<!DOCTYPE= html> <br>
<html> <br>
        <link rel="stylesheet" type="text/css" href="home.css"> <br>
            <ul>
  		<li><a href= home.py''' + cgistuff+ '''">Home</a></li>
  		<li><a class = "active" href="quizzes.py'''+ cgistuff+ '''">Quizzes</a></li>
  		<li><a href="#info">Info</a></li>
  		<li><a href="blogpython.py'''+ cgistuff+ '''">Blog</a></li>
            </ul>
	<title> Star Wars Character Results! </title> <br>
	<body> <br>
		<h3> Star Wars Personality Quiz Results! </h3> <br>

    '''
    form = cgi.FieldStorage()
    questions = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 " , " 6 ", " 7 ", " 8 ", " 9 "]
    allHere = True
    for answer in questions:
        allHere = allHere and answer in form
    if allHere:
        choices()
    else:
        print "Please answer all questions. <br> "
    print '''</p>
	</div>
If you want to try your luck as a different character, Click <a href = "characterquizq.py'''+cgistuff+'''"> here</a> to take the test again or go back to the <a href = "home.py''' +cgistuff+'''"> home page </a>. 
		</body>  
</html>
'''
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

def choices():
    form = cgi.FieldStorage()
    questions = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 " , " 6 ", " 7 ", " 8 ", " 9 "]

    d= {}
    choice1, choice2, choice3, choice4 = 0,0,0,0
    for answers in questions:
        if form[answers].value == " 1 ":
            choice1 += 1
            d["choice1"] = choice1
           
        elif form[answers].value == " 2 ":
            choice2 += 1
            d["choice2"]=choice2
        elif form[answers].value == " 3 ":
            choice3 += 1
            d["choice3"]=choice3
        elif form[answers].value == " 4 ":
            choice4 += 1
            d["choice4"]=choice4
    name = max(d, key= d.get)
    text = open("../data/characters/"+name+".txt", "r")
    text = text.read()
    print text
main()
