#basic if else program

username = "user1"
password = "Pogiako123"

u = input("Input USERNAME-->")

if u == username:
	print("username correct")
else:
	print("incorrect username")

p = input("input PASSWORD-->")

if p == password:
	print("password correct")
	print("welcome", username)
else:
	print("password incorrect")
