import loginHandler

username = input("Please enter username: ")
password = input("Please enter password: ")

isValidUser = loginHandler.loginHandler(username, password)

if(isValidUser == True):
    print("Login success")
else:
    print("Invalid username and password")

