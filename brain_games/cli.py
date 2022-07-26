import prompt

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
# Почему, если в конце файла добавить вызов объявленной функции, то этот вызов дулируется при исполнении модуля ./scripts/brain_games.py, ведь там мы импортировали только саму функцию, а не модуль целиком?
