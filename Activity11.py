import getpass

username = "user1"
password = "Pogiako123"

u = input("Username: ")
p = getpass.getpass("Password: ")

if u == username and p == password:
    print("Login successful!")
else:
    print("Invalid username or password.")