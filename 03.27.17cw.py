def numToWords(n):
    singleslist = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tenslist = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n < 100:
        if n < 20:
            return singleslist[n]
        elif n % 10 != 0:
            return tenslist[n/10-2] + "-" + numToWords(n%10)
        elif n%10 == 0:
            return tenslist[n/10-2]
    elif n < 1000:
        if n %100 != 0:
            return numToWords(n/100) + " hundred and " + numToWords(n%100)
        else:
            return numToWords(n/100) + " hundred"
    elif n < 1000000:
        if n % 1000 != 0:
            return numToWords(n/1000) + " thousand " + numToWords(n%1000)
        else:
            return numToWords(n/1000) + " thousand"
def countletter():
    lettercount = 0
    i = 1
    word = ""
    while i <= 1000:
        word += numToWords(i)
        i += 1
    x = word.count(" ")
    y = word.count("-")
    return len(word) - x - y

def countletterss():
    lettercount = 0
    i = 0
    word = ""
    while i < 1000000:
        word += numToWords(i)
        i += 1
    x = word.count(" ")
    y = word.count("-")
    return len(word) - x - y
