"""Игра - проверка на четность"""


from random import randint


GAME_INSTRUCTIONS = 'Answer "yes" if the number is even, otherwise answer "no".'
LOW_BOUND_OF_NUMBER_SEQUENCE = 1
HIGH_BOUND_OF_NUMBER_SEQUENCE = 50


def is_even(question):
    return question % 2 == 0


def get_question_and_correct_answer():
    question = randint(
        LOW_BOUND_OF_NUMBER_SEQUENCE,
        HIGH_BOUND_OF_NUMBER_SEQUENCE,
    )
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
