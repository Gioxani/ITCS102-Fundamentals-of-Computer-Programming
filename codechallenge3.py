"""
#Global Freight Calc
#Goals
#input in order
#calc using formula
#do not nest if elif else
#pahirapan mo sarili mo use 1 print only
#be productive :)
#pogi na matangkad pa ;)
"""

sender = input("Sender name: ")
type = input("Type of item: ")
frag = input("Fragile Yes/No: ").lower() == "yes"
weight = float(input("Weight: "))
dist = float(input("Distance: "))
fast = input("Express Yes/No: ").lower() == "yes"
intl = input("International Yes/No: ").lower() == "yes"

bCost = weight*2.50 + dist*0.15

if weight <= 2 and dist <=100:
	total_cost = 0.00
elif fast and intl:
	total_cost = bCost*1.40 + 50
elif fast or intl and weight >= 20:
	total_cost = bCost*1.20 + 25
elif weight > 30 or dist > 1000:
	total_cost = bCost + 30
else: total_cost = bCost

print("       SHIPPING SUMMARY\n""Sender        :", sender, "\n""Item          :", type, "\n""Fragile       :", frag, "\n""Weight        :", weight, "kg\n""Distance      :", dist, "km\n""Express       :", fast, "\n""International :", intl, "\n""Total Cost    : $", format(total_cost, ".2f"))


