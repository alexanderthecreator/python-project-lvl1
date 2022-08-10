"""Игра - наибольший общий делитель"""


from random import randint


GAME_INSTRUCTIONS = 'Find the greatest common divisor of given numbers.'
LOW_BOUND_OF_NUMBER_SEQUENCE = 1
HIGH_BOUND_OF_NUMBER_SEQUENCE = 50


def get_gcd(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return str(first_number)


def get_question_and_correct_answer():
    first_number = randint(
        LOW_BOUND_OF_NUMBER_SEQUENCE,
        HIGH_BOUND_OF_NUMBER_SEQUENCE,
        )
    second_number = randint(
        LOW_BOUND_OF_NUMBER_SEQUENCE,
        HIGH_BOUND_OF_NUMBER_SEQUENCE,
        )
    question = f'{first_number} {second_number}'
    correct_answer = get_gcd(first_number, second_number)
    return question, correct_answer
