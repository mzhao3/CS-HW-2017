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
			</div>
	<body>'''


#THIS IS A TEMPLATE TO STAY LOGGED IN BETWEEN PAGES

def mainPage(email,magicNumber):
    #note that ALL links to new pages must include this after the .py 
    cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)
    addReview = '''<br>Click <a href="reviewAdd.py''' + cgistuff + '''">here</a> to add a review!'''
    #see example below:
    if 'movieSearch' in form:
        title = getTitle(form['movieSearch'].value)
        cgistuff += "&title=" + title
        addReview = '''<br>Click <a href="reviewAdd.py''' + cgistuff + '''">here</a> to add a review!'''
        return scrapeData(form['movieSearch'].value) + addReview
    elif 'title' in form:
        title = getTitle(form['title'].value)
        cgistuff += "&title=" + title
        addReview = '''<br>Click <a href="reviewAdd.py''' + cgistuff + '''">here</a> to add a review!'''
        return scrapeData(form['title'].value) + addReview
    return '''  <h1>SEARCH</h1>
    <br>
    <a href="mainpage.py'''+ cgistuff+ '''"> click here </a>to go to the homepage!

    <form method="GET" action="reviewSearch.py">
        Search for a movie! <input type="text" name="movieSearch">
        <input type="hidden" value="''' + email + '''" name="UserEmail">
        <input type="hidden" value="''' + str(magicNumber) + '''" name="magicNumber">
        <input type="submit">
    </form>'''


def getTitle(search):
    list = search.split()
    search = '+'.join(list)
    page = requests.get("http://www.google.com/search?q=" + search)
    content = page.content
    link = ''
    string = 'http://www.imdb.com'
    if 'http://www.imdb.com/title' in content:
        link += content[content.find(string):content.find(string) + 19 + 7 + 9]
        title = link[link.find('tt',25):link.find('tt',25)+9]
        return title
    else:
        return "notitle"

def scrapeData(search):
    list = search.split()
    search = '+'.join(list)
    page = requests.get("http://www.google.com/search?q=" + search)
    returnStatement = ''
    content = page.content
    link = ''
    image = ''
    reviews = ''
    string = 'http://www.imdb.com'
    description = '<meta name="description" content="'
    imageLink = "<link rel='image_src' href="
    if 'http://www.imdb.com/title' in content:
        link += content[content.find(string):content.find(string) + 19 + 7 + 9]
        title = '../data/reviews/' + getTitle(search) + '.txt'
        if not os.path.isfile(title):
            file = open(title, 'a')
            file.write(title.strip('.txt') + '\n')
            file.write('0\n')
            file.close()
            returnStatement += 'No reviews for this movie! Click below to add one!'
        else:
            file = open(title,'r')
            lines = file.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].strip('\n\r\t')
            i = 3
            if len(lines) > 3:
                while i < len(lines):
                    lines[i] = lines[i].split(',')
                    i += 1
                i = 3
                n = 0
                while i < len(lines):
                    reviews += "<h3>" + lines[i][0] + "</h3> said...\n"
                    reviews += "<p>" + lines[i][1] + "</p> <br>"
                    i += 1
        returnStatement += ' <br> Here is the movie result for your search! If it is not right, add it manually by clicking here!'
        page = requests.get(link)
        content = page.content
        image = '<center><img src=' + content[content.find(imageLink)+27: content.find(">", content.find(imageLink)+26)] + 'width="182" height="268"/></center>'
        content = content[content.find(description) + 34: content.find('"',content.find(description) + 35)]
        return HEADER + image + content + reviews + '<br>' + '<br>' + '''<form> <input type="hidden" value="''' + title[title.find('tt'):title.find('tt')+9] +'''" name="title>"
</form>
'''+ returnStatement 
        
    else:
        return 'Could not find link! Click here to add a movie manually'
    
    

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


