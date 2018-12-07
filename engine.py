from board import Board
from tools.printer import Printer

import random
import time

class Engine:
    def __init__(self):
        self.board = Board()
        self.printer = Printer()
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
        coefficient = 1 if self._white_to_play else -1
        all_moves = self.board.possible_move(self._white_to_play)
        for index, move in enumerate(all_moves):
            value = move.evaluate(3, not self._white_to_play)
            if max_value is None or (coefficient * value > coefficient * max_value):
                max_value = value
                best_moves = [move]
            elif value == max_value:
                best_moves.append(move)
        print('board value '+str(max_value))
        self.board = random.choice(best_moves)
        self._white_to_play = 1 - self._white_to_play

    def print_board(self):
        self.printer.print_html(self.board)
