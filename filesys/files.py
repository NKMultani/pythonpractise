#create new text file
#file name demo.txt
#save name in the file 

import os

filename = "demo.txt"

#check if file exists, if not then create
if(not os.path.exists(filename)):
    open(filename, "x")

#write to file
fileToWrite = open(filename, "w")
fileToWrite.write("Hello world!")
fileToWrite.close()

#append to file
fileToAppend = open(filename, "a")
fileToAppend.write("\nHello world again!")
fileToAppend.close()

#append to file
fileToAppendAgain = open(filename, "a")
fileToAppendAgain.write("\nHello world again again!")
fileToAppendAgain.close()

#read file
f = open(filename, "r")
fileContent = f.read()
f.close()
print(fileContent)

#delete file
os.remove(filename)