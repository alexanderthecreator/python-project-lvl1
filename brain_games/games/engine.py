import prompt


def user_greeting():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def game_engine(run_game, GAME_INSTRUCTIONS):
    user_name = user_greeting()
    print(GAME_INSTRUCTIONS)
    correct_answers = 0
    rounds = 3
    while correct_answers < rounds:
        question, correct_answer = run_game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ').lower()
        if correct_answer == user_answer:
            print('Correct!')
            correct_answers += 1
            if correct_answers == 3:
                print(f'Congratulations, {user_name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
