#inputs
age = int(input("Enter your Age-->"))
rev = int(input("Enter Monthly Revenue-->"))
cc = int(input("Enter Credit score-->"))
yrs_b =  int(input("Years Bussines"))
has_defaults = bool(input("Default History"))
collateral = input("Collateral Name")
c_value = float(input("collateral Vaule"))

limit = 0.0
base_fee = 0.0

#baseline
if age >= 21 and yrs_b >=2 and has_defaults == False:
    print("baseline passed")
    #tier 1 condition
    if cc >=720:
        limit = rev * 3
        print("maxloan for high credit is",limit)
        print("High Credit Score of 720")
        if rev >= 720:
            base_fee = limit * 0.015
            print("Base Fee rate is",base_fee)
        else:
            base_fee = limit *0.025
            print("base fee rate is",base_fee)
        if c_value >= limit:#collateral
            print("Collateral", collateral, "--Accepted")
        else:
            print("Collateral not Accepted!!")
        #sercharge
        surcharge = limit * base_fee
        if c_value % 500 !=0:
            surcharge +=250
    
    #tier 2

    elif cc <= 620 and cc < 720:
        limit = rev * 1.5
        print("max laon is set", limit)
        if yrs_b >= 5:
            base_fee = limit * 0.02
            print("Base fee rate is",base_fee)
        else:
            base_fee = limit *0.035
            print("Base fee rate is",base_fee)
        if c_value >= limit:
            print("Collateral", collateral, "-->Accepted")
        else:
            print("Collateralnot accepted!")
        #sercharge
        surcharge = limit * base_fee
        if c_value % 500 !=0:
            surcharge +=250
    #tier 3
    elif cc < 620:
        print("Credit Score too low to low")
    else:
        print("not Tier 1")
else:
    print("Baseline Failed!!")