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

def mainPagesubtract(email,magicNumber,chat_name,newcharacter,what,dowhat):
    #note that ALL links to new pages must include this after the .py 
    cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)

    chatname = "../chatstuff/chats/"+chat_name+".txt"
    chatinfoname = "../chatstuff/chatsinfo/" + chat_name + "info.txt"
    chatusersname = "../chatstuff/chatsusers/" + chat_name + "users.txt"

    if what == "Character":
        stuff = chatinfoname
    if what == "User":
        stuff = chatusersname
    characters = open(stuff, "r").read().split('/n')
    dumb = characters.count("")
    if len(characters)- dumb < 3:
        return basic_html(email,magicNumber,chat_name)
    if not newcharacter in characters:
        return basic_html(email,magicNumber,chat_name)
    
    something = open(stuff, "r").read().split('/n')
    paste = ""
    for i in something:
        if i != newcharacter and i != "":
            paste += i + '/n'
    text = open(stuff, 'w')
    text.write(paste)
    text.close()

    #reader = open("chat.txt").read()
    #print reader
    basic_html(email,magicNumber,chat_name)
    
    
    #see example below:
    return '''  <h1>YOUR PAGE HERE</h1><br>
    ADD CONTENT HERE<br>
    <hr>
    example of a link to some other page that checks login: <br>
    <a href="otherpage.py'''+ cgistuff+ '''"> click here </a>to go to the other page!'''

def mainPageadd(email,magicNumber,chat_name,newcharacter,what,dowhat):
    #note that ALL links to new pages must include this after the .py 
    cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)

    chatname = "../chatstuff/chats/"+chat_name+".txt"
    chatinfoname = "../chatstuff/chatsinfo/" + chat_name + "info.txt"
    chatusersname = "../chatstuff/chatsusers/" + chat_name + "users.txt"

    if what == "Character":
        stuff = chatinfoname
    if what == "User":
        stuff = chatusersname
    characters = open(stuff, "r").read().split('/n')

    if newcharacter in characters:
        return basic_html(email,magicNumber,chat_name)
    
    text = open(stuff, "rw+")
    something = text.read()
    #text.write(something)
    text.write("/n")
    text.write(newcharacter)
    text.close()

    #reader = open("chat.txt").read()
    #print reader
    basic_html(email,magicNumber,chat_name)
    
    
    #see example below:
    return '''  <h1>YOUR PAGE HERE</h1><br>
    ADD CONTENT HERE<br>
    <hr>
    example of a link to some other page that checks login: <br>
    <a href="otherpage.py'''+ cgistuff+ '''"> click here </a>to go to the other page!'''

def basic_html(email,magicNumber,chat_name):
    print '''<!DOCTYPE HTML>
    <html>
        <head>
            <script type="text/javascript">
                window.location.href = "roleplay_version1.py?UserEmail='''+email+'''&magicNumber='''+str(magicNumber)+'''&chat_name='''+chat_name+'''"
            </script>
            <title>Page Redirection</title>
        </head>
        <body>
            <!-- Note: don't tell people to `click` the link, just tell them that it is a link. -->
            If you are not redirected automatically, follow this <a href="roleplay_version1.py?UserEmail='''+email+'''&magicNumber='''+str(magicNumber)+'''&chat_name='''+chat_name+'''">Click here</a>.
        </body>
    </html>'''



def main():
    form = cgi.FieldStorage()

    #list of all required fieldstorage keys
    requiredFields = ['UserEmail','magicNumber','chat_name','newcharacter','what','dowhat']
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
        print "I'm sorry. The chat file you were trying to see does not exist.<br>Go back and please try another name.<br><a href='./existing_chats.py?UserEmail="+email+"&magicNumber"+magicNumber+"'></a>"
        return

    newcharacter = cgi.escape(form["newcharacter"].value)
    what = form['what'].value
    dowhat = form['dowhat'].value

    #You got here? Great! Show the real page.
    if dowhat == 'add':
        print mainPageadd(email,magicNumber,chat_name,newcharacter,what,dowhat)            
    if dowhat == 'subtract':
        print mainPagesubtract(email,magicNumber,chat_name,newcharacter,what,dowhat)            
    
main()
