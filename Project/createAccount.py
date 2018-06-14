#!/usr/bin/python
print 'content-type: text/html\n'
import cgi
import cgitb
import os
import hashlib
import random
cgitb.enable()


#DO NOT let people create accounts, this is for the site creators
#to use to give accounts to people they want.

#make a subdirectory called data
#in a terminal cd into the project directory and: 
#chmod 777 data
#create accounts
#chmod 700 data

#Alternatively, use filezilla.winSCP to check "W" for write,
#or use the Ubuntu file Manager right click the folder:
#properties -> allow everyone "Read and Write"

#get the fieldStorage
form = cgi.FieldStorage()
print form,"<hr>"

def main():

    #check for all the requirements
    requiredFields = ['newUserEmail','newUserPassword']
    allHere = True
    for req in requiredFields:
            allHere = allHere and req in form

    #only create an account if you have all the required data
    if not allHere:
        print '''<h1>DO NOT let people create accounts</h1>
            <p> this is for the site creators to use to give accounts to people they want.</p><hr>
            <form method="POST" action="createAccount.py">
            <h1>create an account:</h1>
            New User Email:<input type="text" name="newUserEmail">
            New User Password:<input type="password" name="newUserPassword">
            <input type="submit">
            </form>
            '''
        return

    #here you know all the requiremnets are met.

    email = form['newUserEmail'].value
    #pick a name based on a unique identifier like email.
    filename = '../data/accounts/'+email+'.txt'

    #check if file exists
    if os.path.isfile(filename):
        #return when you find a duplicate file
        print "Not allowed to create a second user with the same email."
        return

    #now create an list of strings
    #populate this with the lines of your data file
    writeThis = []

    #add a new line of data for each field.
    #since the required fields are in a list, their order is preserved.
    for key in requiredFields:
            value = form[key].value
            
            if key!="newUserPassword":
                    #if it isn't a password just add the value
                    #you can expand this section 
                    #print "Writing '"+value+"'<br>"
                    writeThis.append(value)
            else:
                    #passwords are special treat them differently
                    #make a hashlib object
                    hasher = hashlib.new('sha256')
                    #add your password to it
                    hasher.update(value)
                    #digest it (turn it into a hash)
                    hash = hasher.hexdigest()
                    #print "The hash is <b>"+hash+"</b><br>"
                    writeThis.append(str(hash))
    #append a random number
    writeThis.append(str(random.randint(10000,1000000)))
    #append a fake IP
    writeThis.append("0.0.0.0");

    #join the list with new lines so we can write it to the file
    writeThis = "\n".join(writeThis)
    #print "about to write:\n"+writeThis+"<br>\n"

    #open, write, and close the output file
    outfile = open(filename,'w')
    outfile.write(writeThis)
    outfile.close()
    print "File written and closed"


main()
