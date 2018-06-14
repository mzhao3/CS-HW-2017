def makeTag(d, tag):
    return "<" + tag + ">" + str(d) + "</" + tag + ">"

#print makeTag("e", "tr")
#print makeTag("b", "b")

def makeRow(row, tag):
    final = "<tr>"
    for i in range(len(row)):
        final = final + makeTag(row [i], tag)
    final = final + "</tr>"
    return final

#print makeRow(['a','b','c','d'], "tr")
#print makeRow([1,2,3,12], "td")

def toHTMLTable(L):
    table =  "<table>" + "\n"
    header = L.pop(0)
    table = table + makeRow(header, "th") + "\n"
    for row in L:
        table = table + makeRow(row,"td") + "\n"
    table = table + "/table"
    return table

print toHTMLTable ( [ ['a','b','c','d'], [1,2,3,12], ['fa','bu','lo','us'] ])
