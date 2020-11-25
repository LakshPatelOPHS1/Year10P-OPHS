# -------------------------------------------------------------------
# Import libraries - Enter below or leave blank
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# Global variables - Enter below or leave blank
# -------------------------------------------------------------------

validChoice = False
userChoice = 0


# -------------------------------------------------------------------
# Sub program - Enter below or leave blank
# -------------------------------------------------------------------

def showMenu():
  print("Option 1")
  print("Option 2")
  print("Option 3")


# -------------------------------------------------------------------
# Main program - Enter below or leave blank
# -------------------------------------------------------------------
while validChoice == False:
  
  # Call Func
  
  showMenu()

  # Get Choice
  
  userChoice = int(input("Enter a choice >>> "))

  # Determine choice
  
  if userChoice >= 1 and userChoice <=3:
    validChoice = True
  # Tell user to try again
  
  else:
    print("Invalid Choice")


print("You entered "+str(userChoice))
