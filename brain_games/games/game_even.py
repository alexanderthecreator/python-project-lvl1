"""Игра - проверка на четность"""


from random import randint


GAME_INSTRUCTIONS = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    question = randint(1, 50)
    print(f'Question: {question}')
    if question % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return correct_answer
