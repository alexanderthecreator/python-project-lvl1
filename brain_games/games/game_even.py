"""Игра - проверка на четность"""

import prompt
from random import randint


def game():
    """Основная логика игры"""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise "no"')
    correct_answers = 0
    result = ""
    while correct_answers < 3:
        question = randint(1, 100)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        #Проверка четности значения переменной принявшей значение случайного числа
        if question % 2 == 0:
            if answer.lower() == 'yes':
                print('Correct!')
                correct_answers = correct_answers + 1
            else:
                print(f"{answer} is wrong answer ;(.\nCorrect answer was 'yes'.\nLet's try again, {name}!")
                break
        #Проверка нечетности значения переменной принявшей значение случайного числа
        elif question % 2 != 0:
            if answer.lower() == 'no':
                print('Correct!')
                correct_answers = correct_answers + 1                
            else:
                print(f"{answer} is wrong answer ;(.\nCorrect answer was 'no'.\nLet's try again, {name}!")
                break
    #Проверка условия количества правленьных ответов
    if correct_answers == 3:
        print(f'Congratulations, {name}!')