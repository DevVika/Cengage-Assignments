"""

Author: Viktoriya Kramar
Program: kramarGrades.py
Last Date Modified: 8/3/2025

This program sorts the names of people in alphabetical order and then displays them
along with taking their grades to compute the class average, highest grade, and lowest grade.

"""
# Hardcode file
f1 = open("/workspaces/Cengage-Assignments/grades1.txt", 'r')

# Create two lists to store names and grades
names = []
grades = []

# Grab the first and last names, grades, and store them in list
for line in f1:
    words = line.split()
    first_name = words[0]
    last_name = " ".join(words[1:-1])
    grade = float(words[-1])
    names.append(last_name + "," + first_name)
    grades.append(grade)
# Sort alphabetically
names.sort()

# Print the header
print(f"\n{'First Name':<12} {'Last Name':<12}\n")

# Flip the first and last names again for printing
for name in names:
    words = name.split(',')
    last_name = words[0]
    first_name = words[1]
    # Format and print names
    print(f"{first_name:<12} {last_name:<12}")

# Calculate average scores, also lowest and highest
average = sum(grades) / len(grades)
lowest = min(grades)
highest = max(grades)

# Print the grades
print("\nClass Average: ", average)
print("Highest Grade: ", highest)
print("Lowest Grade: ", lowest)
f1.close()
