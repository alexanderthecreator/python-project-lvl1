"""Игра - Арифметическая прогрессия"""


from random import randint


GAME_INSTRUCTIONS = 'What number is missing in the progression?'


def game():
    first_number = randint(1, 10)
    progression_interval = randint(1, 5)
    progression_length = randint(5, 20)
    progression_next_index = first_number
    progression = [first_number]
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
    correct_answer = str(progression[index - 1] + progression_interval)
    return correct_answer
