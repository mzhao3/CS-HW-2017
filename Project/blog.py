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

form = cgi.FieldStorage()

var = form['comment'].value
var = cgi.escape(var)
email = form['UserEmail'].value
filename = '../data/forum/'+ 'forum' +'.txt'

def makePost(var,email):
    writeThis = email + ': ' + var + '<br>' + '\n'
    outfile = open(filename,'a')
    outfile.write(writeThis)
    outfile.close()

makePost(var,email)

filename = '../data/forum/'+ 'forum' +'.txt'
file = open(filename, "r")
text = file.read()

def mainPage(email,magicNumber):
    #note that ALL links to new pages must include this after the .py 
    cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)
    #see example below:
    print """<!DOCTYPE=html> 
            <html> 
            <head> 
            <link rel="stylesheet" type="text/css" href="blog.css"> 
            <ul>
  		<li><a href= "home.py""" + cgistuff+ """">Home</a></li>
  		<li><a href="quizzes.py"""+ cgistuff+ """">Quizzes</a></li>
  		<li><a href="#info">Info</a></li>
  		<li><a class = "active" href="blogpost.py"""+ cgistuff+ """">Blog</a></li>
            </ul>
            <title> Star Wars Chat </title> <br>
            </head> <br>
            <body background="blog.jpg">
            <form method="Get" action="blog.py">
            """
    print text        
    print        '''    <textarea rows="3" name ="comment" cols = "20">Write a comment here! </textarea> <br>
                    <input type="submit" name = "submit" value = "I'm done"> <br>
                    <input type="hidden" value="''' + email + '''" name="UserEmail">
                    <input type="hidden" value="''' + str(magicNumber) + '''" name="magicNumber">
            '''
def main():
    form = cgi.FieldStorage()
    print form

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

main()

