username = "admin"
password = "pass123"
secret_code = "7777"

u = input("Enter username: ")
p = input("Enter password: ")
s = input("Enter secret code: ")

if u == username and p == password and s == secret_code:
    print("Welcome! Login successful.")

elif u != username and p != password and s != secret_code:
    print("Access denied.")

elif u != username:
    print("Username not found.")

elif p != password:
    print("Incorrect password.")

elif s != secret_code:
    print("Wrong secret code.")