def loginHandler(username, password):
    # if username = admin and password = p@55w03D then success
    lowercaseUsername = username.lower()
    if lowercaseUsername == "admin" and password == "p@55w03D":
        return True
    else:
        return False