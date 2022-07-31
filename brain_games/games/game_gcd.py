"""Игра - наибольший общий делитель"""

import prompt
from random import randint, choice


print('Welcome to the Brain Games!')
user_name= prompt.string('May I have your name? ')
print(f'Hello, {user_name}!')

def find_gcd(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return first_number


def game():
    print('Find the greatest common divisor of given numbers.')
    correct_answers = 0
    while correct_answers < 3:
        first_number = randint(1, 50)
        second_number = randint(1, 50)
        print(f'Question: {first_number} {second_number}')
        correct_answer = find_gcd(first_number, second_number)
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct!')
            correct_answers = correct_answers + 1
        else:
            print(f"{user_answer} is wrong answer ;(\nCorrect answer was {correct_answer}\nLet's try again, {user_name}!")
            break
#Проверка условия количества правильньных ответов
    if correct_answers == 3:
        print(f'Congratulations, {user_name}!')