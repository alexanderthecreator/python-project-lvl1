#!/usr/bin/env python3

from brain_games.games.game_even import get_question_and_correct_answer
from brain_games.games.game_even import GAME_INSTRUCTIONS
from brain_games.engine import handle_game


def main():
    handle_game(get_question_and_correct_answer, GAME_INSTRUCTIONS)


if __name__ == '__main__':
    main()
