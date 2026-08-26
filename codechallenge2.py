moneyVal = 42374


print("money to deposit >>>", moneyVal)


oneThousand = moneyVal//1000
moneyVal = moneyVal - oneThousand*1000
fiveHundred = moneyVal//500
moneyVal = moneyVal - fiveHundred*500
twoHundred = moneyVal//200
moneyVal = moneyVal -  twoHundred*200
oneHundred = moneyVal//100
moneyVal = moneyVal - oneHundred*100
fifty = moneyVal//50
moneyVal = moneyVal - fifty*50
twenty = moneyVal//20
moneyVal = moneyVal - twenty*20
ten = moneyVal//10
moneyVal = moneyVal - ten*10
five = moneyVal//5
moneyVal = moneyVal - five*5
one = moneyVal//1
moneyVal = moneyVal - one*1

print("MONEY DEPOSIT BREAKDOWN")

print("bills count ₱1,000 :", oneThousand)
print("bills count ₱500   :", fiveHundred)
print("bills count ₱200   :", twoHundred)
print("bills count ₱100   :", oneHundred)
print("bills count ₱50    :", fifty)
print("coins count ₱20    :", twenty)
print("coins count ₱10    :", ten)
print("coins count ₱5     :", five)
print("coins count ₱1     :", one)


#sir mas madali pag gagamit ng f-string
"""
print("   MONEY DEPOSIT BREAKDOWN")
print(f"₱1,000 bills : {oneThousand}")
print(f"₱500 bills   : {fiveHundred}")
print(f"₱200 bills   : {twoHundred}")
print(f"₱100 bills   : {oneHundred}")
print(f"₱50 bills    : {fifty}")
print(f"₱20 bills    : {twenty}")
print(f"₱10 bills    : {ten}")
print(f"₱5 coins     : {five}")
print(f"₱1 coins     : {one}")
"""


