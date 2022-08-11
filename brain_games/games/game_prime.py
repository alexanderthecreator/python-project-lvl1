"""Игра - Простое ли число"""


from random import randint


GAME_INSTRUCTIONS = (
    'Answer "yes" if given number is prime.'
    + ' Otherwise answer "no".'
)
LOW_BOUND_OF_NUMBER_SEQUENCE = 1
HIGH_BOUND_OF_NUMBER_SEQUENCE = 500


def is_prime(question):
    for divider in range(2, question // 2 + 1):
        if question % divider == 0 and question != 2:
            return False
        #else:
            #return True


def get_question_and_correct_answer():
    question = randint(
        LOW_BOUND_OF_NUMBER_SEQUENCE,
        HIGH_BOUND_OF_NUMBER_SEQUENCE,
    )
    while question <= 1:
        question = randint(
            LOW_BOUND_OF_NUMBER_SEQUENCE,
            HIGH_BOUND_OF_NUMBER_SEQUENCE,
        )
    if is_prime(question) is False:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return question, correct_answer
