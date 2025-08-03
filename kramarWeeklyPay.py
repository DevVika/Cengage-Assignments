"""

Program: kramarWeeklyPay.py
Author: Viktoriya Kramar
Last date modified: 7/14/2025

This program takes a user's name, rate of pay, and hours worked as input.
Then it outputs the weekly pay for the user.

"""

name = input("Please enter your name: ")
rate_of_pay = float(input("Please enter your rate of pay: "))
hours = float(input("Please enter the number of hours you worked this week: "))

weeklyPay = rate_of_pay * hours

print("\n", name, ", your weekly pay is: $%.2f" % weeklyPay, sep ='')
