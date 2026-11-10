from getpass import getpass
islogin = False
loginattempts = 0

u = "admin"
p = "admin"

while islogin == False:
    uname = input("Enter your username: ")
    pword = getpass("Enter your password: ")

    if uname == u and pword == p:
        print("Login successful!")
        print("Total login attempts:", loginattempts)
        islogin = True
    else:
        print("Login failed. Please try again.")
        loginattempts += 1
        islogin = False
