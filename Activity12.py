# Multiple if and elif conditions
# Create a python program that would capture age group

name = input("Please input your name: ")

age = int(input("Please input your age: "))

if age >= 0 and age <= 1:
    print("That age is considered as NEWBORN")

elif age >= 2 and age <= 3:
    print("That age is considered as TODDLER")

elif age >= 4 and age <= 12:
    print("That age is considered as CHILD")

elif age >= 13 and age <= 17:
    print("That age is considered as TEENAGER")

elif age >= 18 and age <= 59:
    print("That age is considered as ADULT")

elif age >= 60:
    print("That age is considered as ELDERLY")

else:
    print("Age invalid")
