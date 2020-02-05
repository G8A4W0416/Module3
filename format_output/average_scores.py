def average():
    score_1_input = input("Please enter a score out of 100: ")
    score_2_input = input("Please enter another score out of 100: ")
    score_3_input = input("Please enter another score out of 100: ")
    total_score = int(score_1_input) + int(score_2_input) + int(score_3_input)
    average_score = total_score / 3

    return average_score
