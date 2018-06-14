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

def mainuserinfo(mainuser,chat_name):
    mainuserinfo = open(mainuser).readlines()
    mainuserinfo[6] += " " + chat_name
    "/n".join(mainuserinfo)
    mainuserinfo.close()
    print mainuserinfo
    return mainuserinfo

def mainPage(email,magicNumber,chat_name,character1,character2,user):
    #note that ALL links to new pages must include this after the .py 
    cgistuff = "?UserEmail=" + email + "&magicNumber=" + str(magicNumber)
    #see example below:

    chatname = "../chatstuff/chats/"+chat_name+".txt"
    chatinfoname = "../chatstuff/chatsinfo/"+chat_name+"info.txt"
    chatusersname = "../chatstuff/chatsusers/"+chat_name+"users.txt"
    mainuser = "../users/"+email+".txt"
    otheruser = "../users/"+user+".txt"
    
    chat = open(chatname, 'w+')
    chat.write("<p>Welcome to the chat. Enjoy!</p>")
    chat.close()

    chatinfo = open(chatinfoname, "w+")
    chatinfo.write(character1)
    chatinfo.write('/n')
    chatinfo.write(character2)
    chatinfo.close()

    chatusers = open(chatusersname, "w+")
    chatusers.write(email)
    chatusers.write('/n')
    chatusers.write(user)
    chatusers.close()

    '''
    mainuserinfo = open(mainuser).readlines()
    mainuserinfo[6] += " " + chat_name
    "/n".join(mainuserinfo)
    mainuserwrite = open(mainuser, 'w')
    mainuserwrite.truncate()
    mainuserwrite.write(str(mainuserinfo))
    mainuserwrite.close()

    otheruserinfo = open(otheruser).readlines()
    otheruserinfo[6] += " " + chat_name
    otheruserwrite = open(otheruser, 'w')
    otheruserwrite.truncate()
    "\n".join(otheruserinfo)
    otheruserwrite.write(str(otheruserinfo))
    otheruserwrite.close()
    '''
    
    return '''<!DOCTYPE HTML>
    <html>
        <head>
            <script type="text/javascript">
                window.location.href = "existing_chats.py''' + cgistuff +'''"
            </script>
            <title>Page Redirection</title>
        </head>
        <body> 
            <a href="existing_chats.py'''+cgistuff+'''">Click this if you aren't redirected automatically.</a>.
        </body>
    </html>'''

def main():
    form = cgi.FieldStorage()

    #list of all required fieldstorage keys
    requiredFields = ['UserEmail','magicNumber','chat_name','character1','character2','user']
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

    chat_name = form['chat_name'].value
    chatname = "../chatstuff/chats/"+chat_name+".txt"
    if os.path.isfile(chatname):
        print "I'm sorry. The chat file you were trying to create already exists.<br>Please try another name."
        return

    character1 = form['character1'].value
    character2 = form['character2'].value
    user = form['user'].value

    #You got here? Great! Show the real page.
    print mainPage(email,magicNumber,chat_name,character1,character2,user)            
main()
