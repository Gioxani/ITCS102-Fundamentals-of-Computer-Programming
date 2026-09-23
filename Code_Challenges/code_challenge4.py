
import getpass

correct_username = "Gian067"
correct_password = "kaluo760"

username = input("Username: ")
password = getpass.getpass("Password: ")

if username == correct_username and password == correct_password:
    print("Login successful")

    age = int(input("Age: "))
    is_employed = bool(input("Employed? yes/no: ").lower() == "yes")

    credit_score = int(input("Credit score: "))
    annual_income = float(input("Annual income: "))

    has_collateral = bool(input("Has collateral? yes/no: ").lower() == "yes")

    if age >= 21 and is_employed:
        print("Eligible for credit")

        if credit_score >= 750:
            interest_rate = 5.0

            if annual_income >= 100000:
                interest_rate = 4.5

            print("Approved at", interest_rate, "% interest")

        elif credit_score >= 600:
            interest_rate = 8.0

            if has_collateral:
                interest_rate = 7.0

            elif annual_income < 40000:
                interest_rate = 9.5

            print("Approved at", interest_rate, "% interest")

        else:
            print("Rejected: Credit score too low")

    else:
        print("Rejected: Fails baseline criteria")

else:
    print("Access denied: Incorrect username or password")