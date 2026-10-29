'''
        *
      *   *
    *   *   *
  *   *   *   *
    *   *   *
      *   *
        *
'''

size = 4
#1st part(upper)
for g in range(1, size + 1):
    print(" " * (2 * (size - g)) + "*   " * g)

#last part(bottom)
for g in range(size - 1, 0, -1):
    print(" " * (2 * (size - g)) + "*   " * g)
