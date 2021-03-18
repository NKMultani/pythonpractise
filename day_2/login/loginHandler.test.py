import loginHandler

# test cases
print(loginHandler.loginHandler("admin", "p@55w03D")) # True
print(loginHandler.loginHandler("Admin", "p@55w03D")) # True

print(loginHandler.loginHandler("admin", "P@55w03D")) # False
print(loginHandler.loginHandler("user123", "P@55w03D")) # False
print(loginHandler.loginHandler("admin", "password")) # False

