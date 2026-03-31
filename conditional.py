username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin123":
    print("Login successful")
elif username == "admin" and password != "admin123":
    print("Incorrect password")
elif username != "admin" and password == "admin123":
    print("Incorrect username")
else:
    print("Incorrect username and password")