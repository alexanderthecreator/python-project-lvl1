"""Игра - Простое ли число"""

import prompt
from random import randint

print('Welcome to the Brain Games!')
user_name= prompt.string('May I have your name? ')
print(f'Hello, {user_name}!')

def game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        question = randint(1, 1000)
        for divider in range(2, question):
            if question % divider == 0:
                correct_answer = 'no'
                break
            else:
                correct_answer ='yes'
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer.lower() == correct_answer:
            print('Correct!')
            correct_answers = correct_answers + 1
        else:
            print(f"{user_answer} is wrong answer ;(.\nCorrect answer was {correct_answer}.\nLet's try again, {user_name}!")
            break
    #Проверка условия количества правленьных ответов
    if correct_answers == 3:
        print(f'Congratulations, {user_name}!')