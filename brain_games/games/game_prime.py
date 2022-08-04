"""Игра - Простое ли число"""


from random import randint


GAME_INSTRUCTIONS = (
    'Answer "yes" if given number is prime.'
    + ' Otherwise answer "no".'
)


def run_game():
    question = randint(1, 1000)
    correct_answer = "yes"
    while question == 1 or question == 0:
        question = randint(1, 1000)
    else:
        for divider in range(2, question // 2 + 1):
            if question % divider == 0 and question != 2:
                correct_answer = 'no'
                break
    return question, correct_answer
