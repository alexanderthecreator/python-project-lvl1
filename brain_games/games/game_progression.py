"""Игра - Арифметическая прогрессия"""


from random import randint


GAME_INSTRUCTIONS = 'What number is missing in the progression?'


def run_game():
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
    correct_answer = str(progression[progression_random_index])
    progression[progression_random_index] = '..'
    progression = [str(i) for i in progression]
    question = " ".join(progression)
    return question, correct_answer
