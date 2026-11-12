#task 1
loan = float(input("How much loan: "))
years = int(input("How many years: "))

months = years * 12
prin = loan / months
bal = loan
print(f"Months\t\tMonthly Payment\t\tInterest\t\tPrincipal\t\tRemaining Loan")
for mon in range(1, months + 1):
  interest = bal * 0.03 / 12
  payment = prin + interest
  bal = bal - prin
  if bal < 0.005:
    bal = 0
  print(f"{mon}\t\t{round(payment, 2)}\t\t\t{round(interest, 2)}\t\t\t{round(prin, 2)}\t\t\t{round(bal, 2)}")
#task 2
r = int(input("input size of triangle: "))
for x in range(r - 1):
  for y in range(2 * r - 1):
    if y == r - 1 - x or y == r - 1 + x:
      print("*", end= " ")
    else:
      print(" ", end= " ")
  print()
print("* " * (2 * r - 1))
#task 3
r = int(input("Input size of Z:"))
for x in range(r):
  for y in range(r):
    if x == 0 or x == r -1 or y == r -1 -x:
      print("*", end= " ")
    else:
      print(" ", end= " ")
  print()
