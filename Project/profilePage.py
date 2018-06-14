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


#THIS IS A TEMPLATE TO STAY LOGGED IN BETWEEN PAGES
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
				<a href='homepage.html'>Log Out/Home</a>
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
			</div>
	<body>'''

def mainPage(email,magicNumber):
    #note that ALL links to new pages must include this after the .py 
    cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)
    #see example below:
    return HEADER +  '''<h1>PROFILE</h1>''' + str(displayProfile(email, magicNumber)) + '<a href="mainpage.py' + cgistuff + '"> </br> home </a>'

def displayProfile(email, magicNumber):
    filename = '../data/' + email + '.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split('\n')
    info = []
    info.append(lines[0][0])
    info.append(lines[5][0])
    info[1] = info[1].split(',')
    info = [info[0]] + info[1]
    page = requests.get("http://www.imdb.com/title/" + info[1])
    content = page.content
    string = "<title>"
    title = content[content.find(string)+7:content.find("-", content.find(string))]
    info.append(title[0:len(title)-1])
    return info

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



