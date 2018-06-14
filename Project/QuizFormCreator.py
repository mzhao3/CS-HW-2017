#!/usr/bin/python
print 'content-type: text/html\n'
import cgi
import cgitb
cgitb.enable()
form=cgi.FieldStorage()
#print form

quiztype = form.getvalue('Quiz')
if quiztype == "MathQuiz":
    file=open("BasicMathQuizSAMPLE.txt","r")
elif quiztype == "GrammerQuiz":
    file=open("Grammerquiz.txt","r")
data=file.read()
data=data.split('\n')


def MakeQuiztable():
    #creates radio box for question
    rtestqs ='<li><div class="question">'
    rtestqe = '</div></li><br>\n'
    #creates radio boxes for answers
    qtestas = '<input type="radio" name="group'
    qtestaw = '" value="wrong"> '
    qtestawc = '" checked="checked" value="wrong"> '
    qtestac = '" value="correct"> '
    qtestacc = '" checked="checked" value="correct"> '
    qtestae = '<hr>\n'
    i = 1
    j = 0 #j= is the group name number of the radio button
    k = 0
    otext ='<form method="GET" action="quizscorer.py"><br>\n'
    while i < len(data):#goes through the file and puts it in radio question format
        txt = data[i]
        if txt[:2] == '**':#formats question
            otext = otext + rtestqs + txt[2:len(txt)]+rtestqe
            j = j+1
            k=0
        elif txt[:2] == '##':#formats correct answer
            if k==1:
                otext = otext + qtestas + str(j) + qtestacc + txt[2:len(txt)]+ qtestae
            else:
                otext = otext + qtestas + str(j) + qtestac + txt[2:len(txt)]+ qtestae
              
        else:#formats wrong answer
            if k==1:
                otext = otext + qtestas + str(j) + qtestawc + txt + qtestae
            else:    
                otext = otext + qtestas + str(j) + qtestaw + txt + qtestae
        i=i+1
        k=k+1
    return otext+"\n"



msg = ''
msg = msg +"<!DOCTYPE html>\n"
msg = msg +"<html>\n"
msg = msg +"    <head>\n"
msg = msg +"        <title>StuyMedia</title>\n"
msg = msg +"    </head>\n"
msg = msg +"    <body>\n"
msg = msg +"        <h1>StuyMedia</h1>\n"
msg = msg +"        <br>\n"
msg = msg +'        <form method="GET" action="quizscorer.py"><br>'
msg = msg + MakeQuiztable()
msg = msg + "<br>"
msg = msg + "<input type='submit' name='Submit answers'>\n"
msg = msg + "    </form>\n"
msg = msg + "    </body>\n"
msg = msg + "</html>\n"
print msg
