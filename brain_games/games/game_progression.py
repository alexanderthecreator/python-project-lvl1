"""Игра - Арифметическая прогрессия"""


from random import randint


GAME_INSTRUCTIONS = 'What number is missing in the progression?'
LOW_BOUND_OF_PROGRESSION_FIRST_NUMBER = 1
HIGH_BOUND_OF_PROGRESSION_FIRST_NUMBER = 10
LOW_BOUND_OF_PROGRESSION_INTERVAL = 1
HIGH_BOUND_OF_PROGRESSION_INTERVAL = 5
LOW_BOUND_OF_PROGRESSION_LENGHT = 5
HIGH_BOUND_OF_PROGRESSION_LENGHT = 20


def get_question_and_correct_answer():
    first_number = randint(
        LOW_BOUND_OF_PROGRESSION_FIRST_NUMBER,
        HIGH_BOUND_OF_PROGRESSION_FIRST_NUMBER,
    )
    progression_interval = randint(
        LOW_BOUND_OF_PROGRESSION_INTERVAL,
        HIGH_BOUND_OF_PROGRESSION_INTERVAL,
    )
    progression_length = randint(
        LOW_BOUND_OF_PROGRESSION_LENGHT,
        HIGH_BOUND_OF_PROGRESSION_LENGHT,
    )
    progression_next_index = first_number
    progression = []
    i = 0
    while i < progression_length:
        progression.append(str(
            progression_next_index + progression_interval * i,
        ),
        )
        i += 1
    progression_random_index = randint(1, progression_length - 1)
    correct_answer = progression[progression_random_index]
    progression[progression_random_index] = '..'
    question = ' '.join(progression)
    return question, correct_answer
