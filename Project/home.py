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
    return ''' <html>
<head>
	<link rel="stylesheet" type="text/css" href="home.css">
	<ul>
  		<li><a class = "active href= home.py''' + cgistuff+ '''">Home</a></li>
  		<li><a href="quizzes.py'''+ cgistuff+ '''">Quizzes</a></li>
  		<li><a href="#info">Info</a></li>
  		<li><a href="blogpost.py'''+ cgistuff+ '''">Blog</a></li>
	</ul>
	<title> Star Wars </title>
</head>
	<h1> Homepage </h1>
	<p>Animated search form:</p>
	<form>
  		<input type="text" name="search" placeholder="Search..">
	</form>
	<h2> Star Wars </h2>
<body background="../data/aesthetics/homee.jpg"><body> 
	<img src="../data/aesthetics/middle.gif">
	</body>  
</html>'''

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
