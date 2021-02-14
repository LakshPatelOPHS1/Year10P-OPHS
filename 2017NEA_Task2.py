print("League registration")

# Variables

loop = True
currency = "£"
BASE_CHARGE = float(10)
addCharge = float(0)

while loop:

    # Get info

    email = input("Enter your email address >>> ")
    country = input("Enter your country UK/AU/US >>> ").upper()
    skill = input("Enter your skill level. E for Expert, C for Casual >>> ").upper()

    # Calc price

    if skill == "E":
        skill = "Expert"
        addCharge = 35

    else:
        skill = "Casual"
        addCharge = 20

    totalCharge = addCharge + BASE_CHARGE

    if country == "UK":
        pass

    elif country == "AU":
        currency = "$"
        totalCharge *= 2

    elif country == "US":
        currency = "$"
        totalCharge *= 1.5

    print(currency + str(totalCharge))
    verify = str(input("Calculate another price? Y or N")).upper()

    if verify == "Y":
        loop = True
    else:
        loop = False

print("Bye")
