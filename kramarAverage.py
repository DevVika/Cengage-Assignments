"""

Program: kramarAverage.py
Author: Viktoriya Kramar
Last Date Modified: 7/18/25

This program calculates	the	average	of all quiz grades entered by the user
and	prints the total number	of	quizzes, quiz total, lowest	quiz grade and quiz	
average

"""

# Get the first quiz grade before the loop
currentScore = int(input("Enter quiz grade (-77 to end): "))

# Check if the first score is the -77
if currentScore == -77:
    print("No quiz grades have been entered.")
else:
    totalQuizzes = 1
    lowestScore = currentScore
    total = currentScore
    # Gets the lowest test score
    while True:
        currentScore = int(input("Enter quiz grade (-77 to end): "))
        if currentScore == -77:
            break
        if currentScore < lowestScore:
            lowestScore = currentScore
        total += currentScore
        totalQuizzes += 1
   
    # Get the average
    average = total / totalQuizzes
    round(average, 2)
    print("\n\nTotal number of quizzes: ", totalQuizzes)
    print("Quiz total: ", total)
    print("Lowest quiz grade: ", lowestScore)
    print("\n\nQuiz Average: ", average)
