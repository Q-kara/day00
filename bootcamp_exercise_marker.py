# Abdur-Raheem Lee <abdur-raheem@wethinkcode.co.za>
import random

def read_file():
    '''
    Reads contents from the text file (questions.txt)
    @return a list of five random questions
    '''
    with open('questions.txt') as f:
        lines = f.readlines()

    for i in range(1,4):
        lines.remove("\n")

    for i in range(3):
        choice = random.choice(lines)
        print(choice)
        lines.remove(choice)

    return lines


def ask_questions(list_of_questions):
    '''
    Sends quesions one at a time to be displayed
    @param list of five questions
    @return a list of questions the user answer incorrectly
    '''
    incorrect_answers = []
    for i in range(0, len(list_of_questions)):
        answer = display_question(i+1, list_of_questions[i])
        split_string = list_of_questions[i].split(", ")
        correct_answer = split_string[1]
        if(is_correct_answer(correct_answer, answer) == False):
            incorrect_answers.append(list_of_questions[i])

    return incorrect_answers


def display_question(question_number, question):
    '''
    Displays a single question from the list of questions
    Takes in an answer
    @param a single question
    @return the answer given by the user
    '''
    split_string = question.split(", ")
    final_question = str(question_number) + ". " + split_string[0] +"\n"+split_string[2]+"\n"+split_string[3]+"\n"+split_string[4]
    print(final_question)
    valid_answers = ['A','B','C']
    answer = input()
    return answer


def is_correct_answer(solution, user_answer):
    '''
    Checks if the answer given by the user is correct
    @param solution - The correct answer
    @param user_answer - The answer entered by the user
    @return boolean indicating if user answered correctly or not
    '''
    return solution == user_answer


def next_round(current_round):
    '''
    Calculates the next round
    @param current round completed
    @return integer next round
    '''
    return current_round + 1


if __name__ == '__main__':

    score = 0
    current_round = 0
    question_list = read_file()

    while score < 5:
        current_round = next_round(current_round)
        question_list = ask_questions(question_list)
        score = 5 - len(question_list)
