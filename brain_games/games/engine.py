import prompt


def user_greeting():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name

def game_engine(game, GAME_INSTRUCTIONS):
    user_name = user_greeting()
    print(GAME_INSTRUCTIONS)
    correct_answers = 0
    while correct_answers < 3:
        correct_answer = game()
        user_answer = prompt.string('Your answer: ').lower()
        if correct_answer == user_answer.lower():
            print('Correct!')
            correct_answers += 1
            if correct_answers == 3:
                print(f'Congratulations, {user_name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            break