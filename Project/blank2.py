#! /usr/bin/python
print ("content-type: text/html \n")
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

file = open("TableText.txt","r")
text = file.read()
text = text.replace("\t"," ")
text = text.split("\n")
#print (text)

state = form.getvalue("State")
#print state

private = form.getvalue("Private")
#print private

public = form.getvalue("Public")
#print public

searchbar = form.getvalue("Search For Your College")
#print searchbar

def htmlcode():
    print """<DOCTYPE! html><html>
	<html>
	<head>  <title>Crime In College</title> </head>
	<body>
	<h1> Results </h1>
	<form method='GET' action='Important2.py'>"""

def htmlcoding2():
        print "</div>\n</body>\n</html>"

def searchcode(text):
    file = open("TableText.txt","r")
    text = file.read()
    text = text.replace("\t"," ")
    text = text.split("\n")
    a = 0
    while a < len(text):
        texts = text[a]
        a = a + 1
    return texts

def searchcode2():
    file = open("TableText.txt","r")
    text = file.read()
    text = text.replace("\t"," ")
    text = text.split("\n")
    a = 0
    storage = []
    while a < len(text):
        if text == searchbar:
            storage = storage + text
            a = a + 1
        else:
            text = text[a]
            a = a + 1
    print """<p style="text-align:center"> storage </p>"""

def typesearch():
    file = open("TableText.txt","r")
    text = file.read()
    text = text.replace("\t"," ")
    text = text.split("\n")
    a = 0
    storage = []
    while a < len(text):
        if text == private:
            storage = storage + text
            a = a + 1
        else:
            text = text[a]
            a = a + 1
    print """<p style="text-align:center"> storage </p>"""

def statesearch(state):
    file = open("TableText.txt","r")
    text = file.read()
    text = text.replace("\t"," ")
    text = text.split("\n")
    a = 0
    storage = []
    while a < len(text):
        if text == state:
            storage = storage + text
            a = a + 1
        else:
            text = text[a]
            a = a + 1         
    print """<p style="text-align:center"> storage </p>"""

def main():
    htmlcode()
    searchcode2()
    typesearch()
    statesearch(state)
    htmlcoding2()


main()
    
    
    


    
        


    


    





           



  
  
