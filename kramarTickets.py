"""

Program: kramarTickets.py
Author: Viktoriya
Last date modified: 7/17/25

This program calculates the total price of Vikings tickets based on the tier
and the number of tickets requested. 

"""

# Welcome message
print("\nWELCOME to Vikings Stadium!!!\n")
print("Choose a tier:")
print("%-5s %s" % ("[F]", "Field Level"))
print("%-5s %s" % ("[M]", "Main Level"))
print("%-5s %s" % ("[G]", "Grandstand"))
print("%-5s %s" % ("[B]", "Bleachers\n"))
      

# Take input of the tier and number of tickets
print("(Tip: Make sure there are no spaces before or after your input)")
tier = input("Enter F, M, G, or B: ") # <- I just had to take this clever design
TICKETS = int(input("Enter the number of tickets: "))

# Takes both lowercase and uppercase as input!!
if tier == "f" or tier =="F":
    total = TICKETS * 225.25
elif tier == "m" or tier == "M":
    total = TICKETS * 110.75
elif tier == "g" or tier == "G":
    total = TICKETS * 65.50
elif tier == "b" or tier == "B":
    total = TICKETS * 50

# Prints the total
print("Your day of amazing Vikings baseball will cost: ", "$%.2f" % (total),"\n")
