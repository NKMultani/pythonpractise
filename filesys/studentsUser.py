import os

filename = "students.txt"

if(not os.path.exists(filename)):
    open(filename, "x")

firstName = input("enter first name:- ")
lastName = input("enter last name:- ")
email = input("enter Your emial:- ")
dob = input("enter Your dob:- ")
f = open(filename, "a")


f.write("\n" +firstName)
f.write("\n" + lastName)
f.write("\n" + email)
f.write("\n" + dob)

f.write("\n*******************")
f.close()

