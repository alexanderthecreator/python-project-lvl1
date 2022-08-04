#!/usr/bin/env python3

from brain_games.games.game_prime import run_game, GAME_INSTRUCTIONS
from brain_games.games.engine import game_engine


def main():
    game_engine(run_game, GAME_INSTRUCTIONS)


if __name__ == '__main__':
    main()
