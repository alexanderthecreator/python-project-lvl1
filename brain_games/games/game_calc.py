"""Игра - калькулятор"""

import prompt
from random import randint, choice

print('Welcome to the Brain Games!')
user_name= prompt.string('May I have your name? ')
print(f'Hello, {user_name}!')

def game():
    print('What is the result of the expression?')
    correct_answers = 0
    while correct_answers < 3:
        first_member = randint(1, 20)
        operator = choice(["+", "-", "*"])
        second_member = randint(1, 20)        
        if operator == "+":
            print(f'Question: {first_member} {operator} {second_member}')
            user_answer = prompt.string('Your answer: ')
            correct_answer = str(first_member + second_member)
            if correct_answer == user_answer:
                print('Correct!')
                correct_answers = correct_answers + 1
            else:
                print(f"{user_answer} is wrong answer ;(\nCorrect answer was {correct_answer}\nLet's try again, {user_name}!")
                break
        elif operator == "-":               
            while first_member < second_member:
                first_member = randint(1, 20)
                second_member = randint(1,20)    
                if first_member < second_member:
                    continue
                else:
                    print(f'Question: {first_member} {operator} {second_member}')
                    user_answer = prompt.string('Your answer: ')
                    correct_answer = str(first_member - second_member)
                    if correct_answer == user_answer:
                        print('Correct!')
                        correct_answers = correct_answers + 1
                    else:
                        print(f"{user_answer} is wrong answer ;(\nCorrect answer was {correct_answer}\nLet's try again, {user_name}!")
                        break
        elif operator == "*":
            print(f'Question: {first_member} {operator} {second_member}')
            user_answer = prompt.string('Your answer: ')
            correct_answer = str(first_member * second_member)
            if correct_answer == user_answer:
                print('Correct!')
                correct_answers = correct_answers + 1
            else:
                print(f"{user_answer} is wrong answer ;(\nCorrect answer was {correct_answer}\nLet's try again, {user_name}!")
                break

    #Проверка условия количества правленьных ответов
    if correct_answers == 3:
        print(f'Congratulations, {user_name}!')