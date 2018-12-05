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
        elif method == 'human':
            self.play_human()

    def random_play(self):
        self.board = random.choice(self.board.possible_move(self._white_to_play))
        self._white_to_play = 1 - self._white_to_play

    def play_value(self):
        max_value = None
        best_moves = []
        all_moves = self.board.possible_move(self._white_to_play)
        for index, move in enumerate(all_moves):
            value = move.value() * (1 if self._white_to_play else -1)
            if max_value is None or value > max_value:
                max_value = value
                best_moves = [move]
            elif value == max_value:
                best_moves.append(move)

        self.board = random.choice(best_moves)
        self._white_to_play = 1 - self._white_to_play

    def print_board(self):
        time.sleep(2)
        stdscr.addstr(0, 0, 'value {}'.format(self.board.value()))
        for i, line in enumerate(repr(self.board).split('\n')):
            stdscr.addstr(i + 1, 0, line)
        stdscr.refresh()
