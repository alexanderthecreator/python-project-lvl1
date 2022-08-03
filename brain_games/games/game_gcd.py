"""Игра - наибольший общий делитель"""


from random import randint, choice


GAME_INSTRUCTIONS = 'Find the greatest common divisor of given numbers.'


def find_gcd(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return str(first_number)


def game():
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    print(f'Question: {first_number} {second_number}')
    correct_answer = find_gcd(first_number, second_number)
    return correct_answer
