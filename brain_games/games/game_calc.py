"""Игра - калькулятор."""


from random import randint, choice


GAME_INSTRUCTIONS = 'What is the result of the expression?'
LOW_BOUND_OF_NUMBER_SEQUENCE = 1
HIGH_BOUND_OF_NUMBER_SEQUENCE = 20


def get_question_and_correct_answer():
    first_number = randint(
        LOW_BOUND_OF_NUMBER_SEQUENCE,
        HIGH_BOUND_OF_NUMBER_SEQUENCE,
    )
    operator = choice(["+", "-", "*"])
    second_number = randint(
        LOW_BOUND_OF_NUMBER_SEQUENCE,
        HIGH_BOUND_OF_NUMBER_SEQUENCE,
    )
    question = f'{first_number} {operator} {second_number}'
    if operator == '+':
        correct_answer = str(first_number + second_number)
        return question, correct_answer
    elif operator == '-':
        while first_number <= second_number:
            first_number = randint(
                LOW_BOUND_OF_NUMBER_SEQUENCE,
                HIGH_BOUND_OF_NUMBER_SEQUENCE,
            )
            second_number = randint(
                LOW_BOUND_OF_NUMBER_SEQUENCE,
                HIGH_BOUND_OF_NUMBER_SEQUENCE,
            )
            if first_number < second_number:
                continue
        else:
            question = f'{first_number} {operator} {second_number}'
            correct_answer = str(first_number - second_number)
            return question, correct_answer
    elif operator == '*':
        correct_answer = str(first_number * second_number)
        return question, correct_answer
