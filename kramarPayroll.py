"""

Author: Viktoriya Kramar
Program: kramarPayroll.py
Last Date Modified: 7/27/2025

This is a Python program thatopens a file and prints hours,	overtime, and wages	
paid to	each employee for the given	period.

"""

# Hardcode file name
f1 = open("C:\\Users\\vikac\\Downloads\\employeeData.txt", "r")
data = f1.read()
words = data.split()

# Prints the titles
print(f"{'Name':<12} {'Hours':<12} {'Overtime':<12} {'Pay':<12}")

# Loop to get the data
index = 0
while index < len(words):
    name = words[index]
    hours = float(words[index+1])
    wage = float(words[index+2])

    # Calculates the pay
    if hours > 40:
        regular_pay = 40 * wage
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (wage * 1.5)
        pay = overtime_pay + regular_pay
        overtime = "Yes"
    else:
        pay = hours * wage 
        overtime = "No"

    print(f"{name:<12} {str(int(hours)):<12} {overtime:<12} {pay:<12.2f}")

    index += 3

f1.close()
