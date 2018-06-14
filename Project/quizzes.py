#!/usr/bin/python
print 'content-type: text/html\n'
import cgi
import cgitb
import hashlib
cgitb.enable()
import random
import os
import os.path


#THIS IS A TEMPLATE TO STAY LOGGED IN BETWEEN PAGES

def mainPage(email,magicNumber):
    #note that ALL links to new pages must include this after the .py 
    cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)
    #see example below:
    return """<!DOCTYPE=html>
<html>
<head>
	<link rel="stylesheet" type = "text/css" href="home.css">
	<ul>
  		<li><a href= "home.py""" + cgistuff+ """">Home</a></li>
  		<li><a class= "active" href="quizzes.py"""+ cgistuff+ """">Quizzes</a></li>
  		<li><a href="#info">Info</a></li>
  		<li><a href="blogpost.py"""+ cgistuff+ """">Blog</a></li>
	</ul>
	<title> Quizzes </title>
</head>
<body background = "http://wallpapercave.com/wp/ItmVuT6.jpg">
<!-- source: http://wallpapercave.com/star-wars-wallpaper-1920x1080 -->
	<h3> Choose a quiz! </h3>
	<div class= "character"> 
		<p> Sith Lord or Jedi? Find out which Star Wars character YOU are! </p>
		<a href= "characterquizq.py""" + cgistuff + """"> </a>
	</div>
	<div class = "trivia"> 
		<p> Test your Star Wars knowledge with this Trivia quiz! How well do you fare against your friends? </p>
		<a href= "triviaquizq.py""" + cgistuff + """"> </a>
	</div>

</body>
</html>"""


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

