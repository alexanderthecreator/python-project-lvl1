#!/usr/bin/env python3

from brain_games.games import game_calc
from brain_games.engine import handle_game


def main():
    handle_game(game_calc)


if __name__ == '__main__':
    main()
