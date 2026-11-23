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
