print("League registration")

# Get player details.

correct = False

while not correct:

    firstName = str(input("What is your first name >>> "))
    lastName = str(input("What is your last name >>> "))
    nick = str(input("Enter a nickname >>> "))
    skill = input("Enter your skill level. E for Expert, C for Casual >>> ").upper()

    if skill == "E":
        skill = "Expert"
    else:
        skill = "Casual"

    print("\nPlease confirm your details: \n")
    print(f"First name: {firstName}\n Last Name: {lastName}\n Nickname: {nick}\n Skill Level: {skill}\n")

    verify = str(input("Are these details valid? Y or N" )).upper()

    if verify == "Y":
        correct = True
    else:
        correct = False

print("Thanks for registering")
