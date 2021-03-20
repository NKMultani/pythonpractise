class Student:
    def __init__(self, firstname, lastname, age, enrollmentNumber):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.enrollmentNumber = enrollmentNumber


ravlyn = Student("Ravlyn", "Multani", 1, 45655)

print(ravlyn)
print(ravlyn.firstname)
print(ravlyn.lastname)
print(ravlyn.age)
print(ravlyn.enrollmentNumber)