from board import Board

import random
import time
import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

class Engine:
    def __init__(self):
        self.board = Board()
        self._white_to_play = True

    def play(self, method='value'):
        if method == 'random':
            self.random_play()
        elif method == 'value':
            self.play_value()

    def random_play(self):
        self.board = random.choice(self.board.possible_move(self._white_to_play))
        self._white_to_play = 1 - self._white_to_play

    def play_value(self):
        self.board = sorted(
            self.board.possible_move(self._white_to_play), key=lambda b: - self._white_to_play * b.value()
        )[0]
        self._white_to_play = 1 - self._white_to_play


    def print_board(self):
        time.sleep(2)
        stdscr.addstr(0, 0, 'value {}'.format(self.board.value()))
        for i, line in enumerate(repr(self.board).split('\n')):
            stdscr.addstr(i + 1, 0, line)
        stdscr.refresh()
