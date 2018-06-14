#Paste in this code, then test the 3 different read commands.
file = open("data.txt","r")   # r means read mode

#UNCOMMENT ONE of these:
#text = file.read()
text = file.readlines()
#text = file.readline()
print text
