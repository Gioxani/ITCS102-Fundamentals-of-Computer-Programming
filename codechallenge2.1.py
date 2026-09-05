name = input("name:")

print("Welcome!", name)

val = eval(input("deposit money:"))


print("money to deposit >>>",val)


thousand = val//1000
val = val - thousand*1000
fivehundred = val//500
val = val - fivehundred*500
twohundred = val//200
val = val - twohundred*200
onehundred = val//100
val = val - onehundred*100
fifty = val//50
val = val - fifty*50
twenty = val//20
val = val - twenty*20
ten = val//10
val = val - ten*10
five = val//5
val = val - five*5
one = val//1
val = val - one*1

print("Bank Notes Breakdown")
print("1000:", thousand)
print("500 :", fivehundred)
print("200 :", twohundred)
print("100 :", onehundred)
print("50  :", fifty)
print("20  :", twenty)
print("10  :", ten)
print("5   :", five)
print("1   :", one)

val = val + thousand*1000 + fivehundred*500 + twohundred*200 + onehundred*100 + fifty*50 + twenty*20 + ten*10 + five*5 + one

print("total value:", val)