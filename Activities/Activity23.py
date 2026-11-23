#summation program
def my_fact(sagot):
    fact = 1
    for x in range(sagot, 0, -1):
        fact *= x
    return fact    
print("output", my_fact(10))
print("output", my_fact(9))
print("output", my_fact(8))
print("output", my_fact(7))

#snig program
def nips(snig):

    fact = 1

    for gains in range(snig, 0, -1):
        fact *= gains
    return fact

g = int(input("number: "))
print("output: ", nips(g))

#box
size = int(input("Size of box: "))
def square (box):
    for x in range(size):
        for y in range(size):
            if x == 0 or y == 0 or x == size - 1 or y == size - 1:
                print(y, end=" ")
            else:
                print(" ", end=" ")
        print()
    return
print(square(size))
