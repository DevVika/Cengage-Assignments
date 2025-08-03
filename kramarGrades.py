"""

Author: Viktoriya Kramar
Program: kramarGrades.py
Last Date Modified: 8/3/2025

This program sorts the names of people in alphabetical order and then displays them
along with taking their grades to compute the class average, highest grade, and lowest grade.

"""

f1 = open("C:\\Users\\vikac\\AppData\\Local\\Programs\\Python\\Python313\\grades.txt", 'r')

names = []
grades = []

for line in f1:
    words = line.split()
    first_name = words[0]
    last_name = " ".join(words[1:-1])
    grade = words[-1]
    names.append(last_name + "," + first_name)
    grades.append(grade)
names.sort()
for name in names:
    words = name.split(',')
    last_name = words[0]
    first_name = words[1]
    print (first_name + "  " + last_name)
f1.close()
