"""Игра - калькулятор"""


from random import randint, choice


GAME_INSTRUCTIONS = 'What is the result of the expression?'


def game():
    first_member = randint(1, 20)
    operator = choice(["+", "-", "*"])
    second_member = randint(1, 20)        
    if operator == "+":
        print('Question: ', end='')
        print(first_member, operator, second_member, sep=' ')
        correct_answer = str(first_member + second_member)
    elif operator == "-":               
        while first_member < second_member:
            first_member = randint(1, 20)
            second_member = randint(1,20)    
            if first_member < second_member:
                continue
            else:
                print('Question: ', end='')
                print(first_member, operator, second_member, sep=' ')
                correct_answer = str(first_member - second_member)
    elif operator == "*":
        print('Question: ', end='')
        print(first_member, operator, second_member, sep=' ')
        correct_answer = str(first_member * second_member)
    return correct_answer