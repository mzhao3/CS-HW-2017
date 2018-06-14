file = open("datalinux.csv", "r")
data = file.read().split("\n")
header = data.pop(0)
def sumCol(ListOfLists, n):
    sumage = 0
    for line in ListOfLists[:-1]:
        line = line.split(",")
        line[n] = float(line[n])
        sumage = sumage + line[n]
    return sumage
print sumCol(data, 3)

average = sumCol(data,3) / len(data)
print average


def highestscore(ListOfLists, n):
    highest = 0
    for line in ListOfLists[:-1]:
        line = line.split(",")
        line[n] = float(line[n])
        if highest < line[n]:
            highest = line
            print highest
    return highest

print highestscore(data, 4)

text = file.read()
row = text.split('\n')
row.remove('')
def fix(L):
    for j in range(len(L)):
        L[j] = int(float(L[j]))

def highest(row):
    ans = 0
    for s in range(len(row)):
        fix(row[s])
        if ans < row[s][2]:
            ans = row[s][2]
    print ans

highest(text)
