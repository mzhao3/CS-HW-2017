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
def mainPagesubtract(email,magicNumber,chat_name,what,dowhat):
    #note that ALL links to new pages must include this after the .py 
    cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)

    chatname = "../chatstuff/chats/" + chat_name + ".txt"

    text = open(chatname,"r").read()
    '<br>'.join(text.split('\n'))

    chatinfoname = "../chatstuff/chatsinfo/" + chat_name + "info.txt"
    chatusersname = "../chatstuff/chatsusers/" + chat_name + "users.txt"

    if what == 'Character':
        stuff = chatinfoname
    if what == 'User':
        stuff == chatusersname
    characters = open(stuff,'r').read().split('/n')

    text = ""
    for i in characters:
        if i != "":
            text += '<input type="radio" name="newcharacter" value="'+i+'" checked> '+i+'<br>'
    
    #see example below:
    return '''<!DOCTYPE html>
    <html>
    <head><title> Zompirates! </title>
    <link type="text/css" rel="stylesheet" href="../ZompiratesDesign.css"/>
    </head>
    <body>
        <div id="logo">
            <center><img src="http://i.imgur.com/JskcO2E.png" width="100%" height="400px"></center>
        </div>
        <div id="header">
            <center>
                <ul id="header">
	           <li id="head"><a href ="">Quiz</a></li>
	           <li id="head"><a href ="roleplay.py'''+cgistuff+'''">Roleplay</a></li>
	           <li id="head"><a href ="../home.py'''+cgistuff+'''">Home</a></li>
	           <li id="head"><a href ="../accounts/account.py'''+cgistuff+'''">Account</a></li>
	           <li id="head"><a href ="../about.py'''+cgistuff+'''">About</a></li>
                </ul>
        `   </center>
        </div>
        
        <div id="login">
        <p>
		<form method="Get" action="redirect_to_character.py">

		<input type="hidden" name="UserEmail" size="25" value="'''+email+'''">
                <input type="hidden" name="magicNumber" size="25" value="'''+str(magicNumber)+'''">
                <input type="hidden" name="chat_name" size="25" value="'''+chat_name+'''">
                <input type="hidden" name="what" value="Character">
                <input type="hidden" name="dowhat" value="subtract">

		
		New '''+what+''''s Name (Please don't add one that already exists. It will not be accepted.):<br>
		'''+text+'''
		<br><br>

		<input type="submit" name="submited" value="submit">

		</form>
		</p>
        </div>
        </body>
        </html>
    '''

def mainPageadd(email,magicNumber,chat_name,what,dowhat):
    #note that ALL links to new pages must include this after the .py 
    cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)

    chatname = "../chatstuff/chats/" + chat_name + ".txt"

    text = open(chatname,"r").read()
    '<br>'.join(text.split('\n'))

    chatinfoname = "../chatstuff/chatsinfo/" + chat_name + "info.txt"
    characters = open(chatinfoname, "r").read().split('/n')
    lower = what.lower()
    #see example below:
    return '''<!DOCTYPE html>
    <html>
    <head><title> Zompirates! </title>
    <link type="text/css" rel="stylesheet" href="../ZompiratesDesign.css"/>
    </head>
    <body>
        <div id="logo">
            <center><img src="http://i.imgur.com/JskcO2E.png" width="100%" height="400px"></center>
        </div>
        <div id="header">
            <center>
                <ul id="header">
	           <li id="head"><a href ="">Quiz</a></li>
	           <li id="head"><a href ="roleplay.py'''+cgistuff+'''">Roleplay</a></li>
	           <li id="head"><a href ="../home.py'''+cgistuff+'''">Home</a></li>
	           <li id="head"><a href ="../accounts/account.py'''+cgistuff+'''">Account</a></li>
	           <li id="head"><a href ="../about.py'''+cgistuff+'''">About</a></li>
                </ul>
        `   </center>
        </div>
        
        <div id="login">
        <p>
		<form method="Get" action="redirect_to_character.py">

		<input type="hidden" name="UserEmail" size="25" value="'''+email+'''">
                <input type="hidden" name="magicNumber" size="25" value="'''+str(magicNumber)+'''">
                <input type="hidden" name="chat_name" size="25" value="'''+chat_name+'''">
                <input type="hidden" name="what" value="Character">
                <input type="hidden" name="dowhat" value="add">

		
		New '''+what+''''s Name (Please don't add one that already exists. It will not be accepted.):<br>
		<input type="text" name="newcharacter" size="25" value="">
		<br><br>

		<input type="submit" name="submited" value="submit">

		</form>
		</p>
        </div>
        </body>
        </html>
    '''

def basic_html_top():
    return """<!DOCTYPE html>
    <html>
        <head>
            <title>Roleplay</title>
        </head>
        <body>"""
    
def basic_html_bottom():
    return """    </body>
    </html>"""

def printing_chat(text):
    return '<p>', text, '</p>'

def chat_form(email,magicNumber,chat_name):
    return '''<p>
		<form method="Get" action="redirect_to.py">

		<input type="hidden" name="UserEmail" size="25" value="'''+email+'''">
                <input type="hidden" name="magicNumber" size="25" value="'''+str(magicNumber)+'''">
                <input type="hidden" name="chat_name" size="25" value="'''+chat_name+'''">

		Type:
		<input type="text" name="chat_sub" size="25" value="">
		<br>

		<input type="submit" name="submited" value="submit">

		</form>
		</p>'''

def main():
    form = cgi.FieldStorage()

    #list of all required fieldstorage keys
    requiredFields = ['UserEmail','magicNumber','chat_name','what','dowhat']
    allHere = True
    for req in requiredFields:
            allHere = allHere and req in form

    #check for required fields
    if not allHere:
        print "Not logged in properly (not all form elements)."
        return

    #get the name of the data file
    email = form['UserEmail'].value
    filename = "../users/"+email+".txt"

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
    #IP = os.environ["REMOTE_ADDR"]
    #if str(IP)!=storedIP:
    #    print "Not logged in properly (invalid IP)."
    #    return                
    
    chat_name = form["chat_name"].value
    chatname = "../chatstuff/chats/"+chat_name+".txt"
    if not os.path.isfile(chatname):
        print "I'm sorry. The chat file you were trying to see does not exist.<br>Go back and please try another name.<br><a href='./existing_chats.py?UserEmail="+email+"&magicNumber="+magicNumber+"'>Click here.</a>"
        return
    what = form['what'].value
    dowhat = form['dowhat'].value

    #You got here? Great! Show the real page.
    if dowhat == 'add':
        print mainPageadd(email,magicNumber,chat_name,what,dowhat)
    if dowhat == 'subtract':
        print mainPagesubtract(email,magicNumber,chat_name,what,dowhat)
main()
