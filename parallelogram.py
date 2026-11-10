
size = int(input("Enter the size of the parallelogram: "))

for x in range(size):
    print(" " * (size - x - 1), end="")

    for y in range(size):
        if x == 0 or y == 0 or x == size - 1 or y == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
