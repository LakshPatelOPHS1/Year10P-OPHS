# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------



# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------

score = 0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------


#Get first score
score = int(input("Enter a score>>>"))
#Keep looping until user enter a 0

while score != 0:
    if score >= 70:
        print("Distinction")
    elif score >= 60 and score <= 69:
        print("Merit")
    elif score >= 50 and score <= 59:
        print("Pass")
    else:
        print("No Category found")

    #Get next score
    score = int(input("Enter a score>>>"))
print("Goodbye")
