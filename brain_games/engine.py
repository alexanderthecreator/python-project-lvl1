import prompt


GAME_ROUNDS = 3


def greet_user_and_get_his_name():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def handle_game(game):
    user_name = greet_user_and_get_his_name()
    print(game.GAME_INSTRUCTIONS)
    correct_answers = 0
    while correct_answers < GAME_ROUNDS:
        question, correct_answer = game.get_question_and_correct_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ').lower()
        if correct_answer == user_answer:
            print('Correct!')
            correct_answers += 1
            if correct_answers == GAME_ROUNDS:
                print(f'Congratulations, {user_name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
