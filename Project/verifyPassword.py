#!/usr/bin/python
print 'content-type: text/html\n'
import cgi
import cgitb
import hashlib
cgitb.enable()
import random
import os
import os.path


form = cgi.FieldStorage()

requiredFields = ['UserEmail','UserPassword']
allHere = True
for req in requiredFields:
	allHere = allHere and req in form

if allHere:
    email = form['UserEmail'].value
    filename = "../data/accounts/"+email+".txt"
    if os.path.isfile(filename):
        password = form['UserPassword'].value
        userInfo = open(filename).read().split("\n")
        storedHash = userInfo[1]

        hasher = hashlib.new('sha256')
        hasher.update(password)
        inputHash = hasher.hexdigest()
        
        if(storedHash == inputHash):
            #print "Same passwords!<br>"
            #this is where you put information you want to hide behind a login.
            magicNumber = random.randint(100000,1000000)
            userInfo[2] = str(magicNumber)
            IP = os.environ["REMOTE_ADDR"]
            userInfo[3] = str(IP)
            outText = "\n".join(userInfo)
            outFile = open(filename,'w')
            outFile.write(outText)
            outFile.close()
            cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)
            print"""<!DOCTYPE= html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="home.css">
	<ul>
  		<li><a class="active" href= home.py""" + cgistuff+ """">Home</a></li>
  		<li><a href="quizzes.py"""+ cgistuff+ """">Quizzes</a></li>
  		<li><a href="#info">Info</a></li>
  		<li><a href="blogpost.py"""+ cgistuff+ """">Blog</a></li>
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
</html>"""
        else:
            print "<b>Invalid</b> password.<br>"
    else:
        print "No account data found"
