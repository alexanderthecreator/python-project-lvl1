"""Игра - проверка на четность"""


from random import randint


GAME_INSTRUCTIONS = 'Answer "yes" if the number is even, otherwise answer "no".'


def determine_even(question):
    if question % 2 == 0:
        return True
    else:
        return False


def run_game():
    question = randint(1, 50)
    is_even = determine_even(question)
    if is_even is True:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
