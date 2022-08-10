"""Игра - Простое ли число"""


from random import randint


GAME_INSTRUCTIONS = (
    'Answer "yes" if given number is prime.'
    + ' Otherwise answer "no".'
)


def is_prime(question):
    for divider in range(2, question // 2 + 1):
        if question % divider == 0 and question != 2:
            return False


def get_question_and_correct_answer():
    question = randint(1, 1000)
    while question <= 1:
        question = randint(1, 1000)
    if is_prime(question) == False:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return question, correct_answer
