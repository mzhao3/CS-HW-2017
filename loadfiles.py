#Paste in this code, then test the 3 different read commands.
file = open("data.txt","r")   # r means read mode

#UNCOMMENT ONE of these:
#text = file.read()
#text = file.readlines()
#text = file.readline()
#print text


text = file.read().split("\n")
nums = text[2].split()

def sumints(L):
    sums = 0
    for i in range(len(L)):
        sums = sums + int(L[i])
    print sums

sumints(nums)

nums = text[3].split()
def sumfloats(L):
    sums = 0
    for i in range(len(L)):
        sums = sums + float(L[i])
    print sums
sumfloats(nums)

file = open("data2.txt" , "r")

texts = file.read().split("\n")

def fixAll(texts):
    totallist = []
    for i in range(len(texts)):
        texts[i] = texts[i].split(",")
        for j in range(len(texts[i])):
            texts[i][j] = int(texts[i][j])
        totallist = totallist + texts[i]
    return totallist
sumints(fixAll(texts))
