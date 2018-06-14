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
  		<li><a href="blogpost.py'''+ cgistuff+ '''">Blog</a></li>
            </ul>
	<title> Trivia Results </title> <br>
	<body> <br>
		<h3> Trivia Results </h3> <br>
		<h4> Not too shabby!! You are as knowledgable as some of our greatest padawans. <br>
		You are ready to become a Jedi Knight! </h4> <br> 
    '''
    answers = {' 1 ': 'Alderan',' 2 ': 'Kamino', ' 3 ':"It's the most important meme of Star Wars history.", ' 4 ': 'Qui-Gon', ' 5 ': 'He was shot by a blaster.', ' 6 ': 'Scarif', ' 7 ': 'The ineffective constitutional monarchy of the Galactic Republic.', ' 8 ' : 'Anakin', ' 9 ':'Stars', ' 10 ': 'R2-D2'} 
    formdata=cgi.FieldStorage()
    allHere = True
    for answer in answers:
        allHere = allHere and answer in formdata
    if allHere:
        scoreQuiz()
    else:
        print "Please answer all questions."
    print '''Click <a href = "triviaquizq.py'''+cgistuff+'''"> here</a> to retake the quiz and try for a better score! <br> 
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

formdata = cgi.FieldStorage()
ans = []

for key in formdata.keys():
    ans.append(formdata[key].value)
    #what will you do with log in info that's in the fieldstorage?


def response():
    i = 0
    ah = []
    while i < 10:
        i += 1
        ah.append(formdata[' ' + str(i) + ' '].value)
response()        

def scoreQuiz():
        #checks to see if all questions have been answered
    answers = {' 1 ': 'Alderan',' 2 ': 'Kamino', ' 3 ':"It's the most important meme of Star Wars history.", ' 4 ': 'Qui-Gon', ' 5 ': 'He was shot by a blaster.', ' 6 ': 'Scarif', ' 7 ': 'The ineffective constitutional monarchy of the Galactic Republic.', ' 8 ' : 'Anakin', ' 9 ':'Stars', ' 10 ': 'R2-D2'} 
    
        #Answer key
    correct = 0
    i = 1
    while i <= 10:
        if formdata[' ' + str(i) + ' '].value.strip() != answers[' ' + str(i) + ' '].strip():
            print "You got question " + str(i) + " wrong. You answered" + formdata[' ' + str(i) + ' '].value + "when the correct answer was " + answers[' ' + str(i) + ' '] + ". <br>"
            i += 1
        else:
            print "You got question " + str(i) + " correct. <br>"
            i += 1
            correct += 1
    print "You answered " + str(correct) + "/10 questions correctly! <br>"

main()
