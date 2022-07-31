"""Игра - Арифметическая прогрессия"""

import prompt
from random import randint, choice


print('Welcome to the Brain Games!')
user_name= prompt.string('May I have your name? ')
print(f'Hello, {user_name}!')


def progression():
    first_number = randint(1, 10)
    progression_interval = randint(1, 5)
    progression_length = randint(5, 20)
    progression_next_index = first_number
    progression = []
    i = 0
    while i < progression_length:
        progression_next_index = progression_next_index + progression_interval
        progression.append(progression_next_index)
        i += 1
    progression_random_index = randint(1, progression_length - 1)
    progression[progression_random_index] = ".."
    index = progression.index('..')
    print('Question: ', end='')
    print(*progression, sep=" ")
    correct_answer = progression[index - 1] + progression_interval
    return correct_answer


def game():
    print('What number is missing in the progression?')
    correct_answers = 0
    while correct_answers < 3:
        correct = progression()
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct):
            print('Correct!')
            correct_answers = correct_answers + 1
        else:
            print(f"{user_answer} is wrong answer ;(\nCorrect answer was {correct}\nLet's try again, {user_name}!")
            break
    if correct_answers == 3:
        print(f'Congratulations, {user_name}!')
