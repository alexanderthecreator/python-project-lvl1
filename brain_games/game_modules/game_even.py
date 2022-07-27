"""Игра - проверка на четность"""

import prompt
from random import randint
from brain_games.greeting import name


def game():
    print('Answer "yes" if the number is even, otherwise "no"')
    i = 1
    result = ""
    while i <= 3:
        question = randint(1, 100)
        print(f'Question: {question}')
        answer = prompt.string('')
        print(f'Your answer: {answer}')
        if question % 2 == 0:             
            if answer.lower() == 'yes':
                print('Correct!')
                result = "Correct"
            else: 
                print(f'{answer} is wrong answer ;(. Correct answer was "yes"')
        elif question % 2 != 0:
            if answer.lower() == 'no':
                print('Correct!')
                result = "Correct"
            else: 
                print(f'{answer} is wrong answer ;(. Correct answer was "no"')
        if result == "Correct":
            print(f'Congratulations, {name}')
            i = i + 1
        else:
            break
game()
    