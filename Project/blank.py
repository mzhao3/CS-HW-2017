#!/usr/bin/python
print "Content-type: text/html\n"
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()


def makeTag(data, tag):
    return """
    """+ '<' + tag +  '>' + str(data) + '</' + tag + '>' 

def makeRow(data, tag):
    newline = '\n'
    for i in range(len(data)):
        newline = newline + makeTag(data[i], tag)  
    return newline + '\n'

#print makeRow(["a","b","c","d"],"td")
#print makeRow(["1","2","3"],"th")


def createHTMLTable(L):
    tableword = """<table>
    """
    for i in range(len(L)):
            if i == 0:
              tableword = tableword +  "\n <tr>" + makeRow(L[i], 'th') + '\n </tr>'
            else:
                tableword = tableword + "\n <tr>" + makeRow(L[i], 'td') + "\n </tr>"
    return tableword + "\n</table>"


#print toHTMLTable([ ['a','b','c','d'], [1,2,3,12], ['fa','bu','lo','us'] ])


def listOfLists(list):
    i = 0
    while i < len(list):
        list[i] = list[i].split(',')
        i = i + 1
    return list

def fix(list):
    bigList = 1
    littleList = 2
    while bigList < len(list):
        while littleList < len(list[bigList]):
            if list[bigList][littleList] != 's':
                list[bigList][littleList] = int(list[bigList][littleList])
            littleList = littleList + 1
        bigList = bigList + 1
        littleList = 2
    return list


def readFile(filename):
    file = open(filename, "r").read()
    text = file.split('\n')
    text = listOfLists(text)
    return text[0:-1]



def sumScores(list):
    i = 1
    word = ""
    list[0].append('Total Scores')
    while i < len(list):
        if list[i][3] != 's':
            list[i].append(0)
        i = i + 1
    return list

def createHTMLFileComplete(name):
    file = open(name + '.html', "r+")
    file.write("""<DOCTYPE! HTML>
    <html>
        <head>
            <title> Crime In College </title>
        </head>""" + """<body style="background-color: thistle;">
<form method = "GET" action = "Important2.py"
<h1><p style="text-align:center"> Search For Colleges: 
<input type="text" name="Search For Your College" size="20" value="">
</p></h1>
<br/>
<p style="text-align:center"> Below are the crime statistics of colleges and institutions. It is the arrest data for the years 2013-2015. </p>
<h1 style="text-align:center">Filter </h1>    
<p style="text-align:center"> Private 
<input type="checkbox" name="Private" value="Yup">
Public <input type="checkbox" name="Public" value="Yup">
State <select name="State" size="1">
<option selected>All States</option>
<option>AL</option>
<option>AK</option>
<option>AZ</option>
<option>AR</option>
<option>CA</option>
<option>CO</option>
<option>CT</option>
<option>DE</option>
<option>FL</option>
<option>GA</option>
<option>HI</option>
<option>ID</option>
<option>IL</option>
<option>IN</option>
<option>IA</option>
<option>KS</option>
<option>KY</option>
<option>LA</option>
<option>ME</option>
<option>MD</option>
<option>MA</option>
<option>MI</option>
<option>MN</option>
<option>MS</option>
<option>MO</option>
<option>MT</option>
<option>NE</option>
<option>NV</option>
<option>NH</option>
<option>NJ</option>
<option>NM</option>
<option>NY</option>
<option>NC</option>
<option>ND</option>
<option>OH</option>
<option>OK</option>
<option>OR</option>
<option>PA</option>
<option>RI</option>
<option>SC</option>
<option>SD</option>
<option>TN</option>
<option>TX</option>
<option>UT</option>
<option>VT</option>
<option>VA</option>
<option>WA</option>
<option>WV</option>
<option>WI</option>
<option>WY</option>
</select>
<p style="text-align:center"><input type="submit" name="Find" value="Find"></p>
""" + createHTMLTable(sumScores(readFile(name))) + """
        </body>
    </html>""")

createHTMLFileComplete("VeryImportant.csv")
