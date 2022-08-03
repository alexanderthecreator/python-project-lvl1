"""Игра - Простое ли число"""

from random import randint


GAME_INSTRUCTIONS = (
    f'Answer "yes" if given number is prime.{" "}'
    f'Otherwise answer "no".'
)


def game():
    question = randint(1, 1000)
    print(f'Question: {question}')
    for divider in range(2, question):
        if question % divider == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
    return correct_answer
