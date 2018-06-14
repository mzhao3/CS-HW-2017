#!/usr/bin/python
print 'content-type: text/html\n'
import cgi
import cgitb
import hashlib
cgitb.enable()
import random
import os
import os.path
import requests


form = cgi.FieldStorage()
HEADER = '''
<DOCCTYPE! html>

<html>
	
	<head>

		<link type='text/css' rel='stylesheet'
href='stylesheet.css'/>

	</head>
	
		<body>
	
			<h1>StuyMDB</h1>
			<div>
				<a href='homepage.html'>Logout/Home</a>
				<a>
					<select name='genre'
size='1'>
						<option
selected>Movies</option>
						<option>Comedy</option>
						<option>Drama</option>
						<option>Action</option>
					</select>
				</a>
			</div>'''


def mainPage(email,magicNumber):
    #note that ALL links to new pages must include this after the .py 
    cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)
    if 'review' in form:
        return addReview(form['review'].value, email, magicNumber)
    return HEADER + '''<form method="GET" action="reviewAdd.py">
        <input type="hidden" value="''' + email + '''" name="UserEmail">
        <input type="hidden" value="''' + str(magicNumber) + '''" name="magicNumber">
        <input type="hidden" value="''' + str(form['title'].value) + '''" name="title">
        <textarea rows="3" name="review" cols="20"> Enter Review Here!
        </textarea>
        <input type="submit">''' + '''<br>Click <a href="reviewSearch.py''' + cgistuff + "&title=" + form['title'].value + '''">here</a> to go back'''


def addReview(input, email, magicNumber):
    cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)
    filename = '../data/reviews/' + form['title'].value + '.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    file.close()
    if email in str(lines):
        return HEADER + "You can't add another review! If you would like to edit your old one, click on edit" + '''<br>Click <a href="reviewSearch.py''' + cgistuff + "&title=" + form['title'].value + '''">here</a> to go back'''
    elif input in lines:
        return HEADER + "You can't add the same review as another user! Original content please!" + '''<br>Click <a href="reviewSearch.py''' + cgistuff + "&title=" + form['title'].value + '''">here</a> to go back'''
    else:
        
        file = open(filename, 'a')
        file.write('\n' + email + ',' + input)
        file.close()
        file = open('../data/' + email + '.txt', 'a')
        file.write('\n' + form['title'].value + ',' + input)
        return HEADER + '<br>' + '''<br> The following, <strong>''' + input + "</strong>, was added to the reviews! Thank you " + email + "!" + '''<br>Click <a href="reviewSearch.py''' + cgistuff + "&title=" + form['title'].value + '''">here</a> to go back'''


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
    filename = "../data/"+email+".txt"

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
