class User:
    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender 


class Student(User):
    def __init__(self, firstname, lastname, gender, rollNumb):
        User.__init__(self, firstname, lastname, gender)
        self.rollNumb = rollNumb

student = Student("Ravlyn", "Kaur", "F", 5689465)
print("-- Printing Student --")
print(student.firstname)
print(student.lastname)
print(student.gender)
print(student.rollNumb)
print("--------------------")

class Staff(User):
    def __init__(self, firstname, lastname, gender, staffNumb):
        User.__init__(self, firstname, lastname, gender)
        self.staffNumb = staffNumb

staff = Staff("Navdeep", "Kaur", "F", 9898956)
print("-- Printing Staff --")
print(staff.firstname)
print(staff.lastname)
print(staff.gender)
print(staff.staffNumb)    
print("--------------------")    