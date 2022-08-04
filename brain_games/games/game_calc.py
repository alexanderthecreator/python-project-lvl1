"""Игра - калькулятор."""


from random import randint, choice


GAME_INSTRUCTIONS = 'What is the result of the expression?'


def run_game():
    first_number = randint(1, 20)
    operator = choice(["+", "-", "*"])
    second_number = randint(1, 20)
    if operator == "+":
        question = f'{first_number} {operator} {second_number}'
        correct_answer = str(first_number + second_number)
        return question, correct_answer
    elif operator == "-":
        while first_number <= second_number:
            first_number = randint(1, 20)
            second_number = randint(1, 20)
            if first_number < second_number:
                continue
        else:
            question = f'{first_number} {operator} {second_number}'
            correct_answer = str(first_number - second_number)
            return question, correct_answer
    elif operator == "*":
        question = f'{first_number} {operator} {second_number}'
        correct_answer = str(first_number * second_number)
        return question, correct_answer
