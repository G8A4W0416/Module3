"""
Program average_scores.py

Author: Greg Wilhelm

Last date modified: 2/04/2020

The purpose of this program is to prompt the user for their first name, last name, age, and three scores and then
calculate the average of their three scores via a function call. What the user entered and the average of their scores
is then printed at the end.

"""


def average():
    score_1_input = input("Please enter a score out of 100: ")
    score_2_input = input("Please enter another score out of 100: ")
    score_3_input = input("Please enter another score out of 100: ")
    total_score = int(score_1_input) + int(score_2_input) + int(score_3_input)
    average_score = total_score / 3

    return average_score


if __name__ == '__main__':

    first_name = input("Please enter your first name: ")
    last_name = input("Please is your last name: ")
    age = input("Please enter your age: ")
    average_scores = average()

    print(f"{last_name}, {first_name} age: {age} average grade: {average_scores:.2f}")


# Input:            Greg, Wilhelm, 35, 90, 89, 77
# Expected Output:  "Wilhelm, Greg age: 35 average grade: 85.33"
# Actual Output:    "Wilhelm, Greg age: 35 average grade: 85.33"
#
# Input:            Tony, Stark, 49, 100, 100, 100
# Expected Output:  "Stark, Tony age: 49 average grade: 100.00"
# Actual Output:    "Stark, Tony age: 49 average grade: 100.00"
#
# Input:            Bruce, Banner, 50, 16, 100, 0
# Expected Output:  "Banner, Bruce age: 50 average grade: 38.67"
# Actual Output:    "Banner, Bruce age: 50 average grade: 38.67"
