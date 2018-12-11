from board import Board
from tools.printer import Printer

import random
import time


class Engine:
    def __init__(self):
        self.board = Board(method='exercice')
        self.printer = Printer()
        self._color_to_play = 1

    def play(self, method='value', deapth=3):
        if method == 'random':
            self.random_play()
        elif method == 'value':
            self.play_value(deapth)

    def random_play(self):
        self.board = random.choice(self.board.possible_move(self._color_to_play))
        self._color_to_play *= -1

    def play_value(self, depth):
        max_value = None
        best_moves = []
        all_moves = self.board.possible_move(self._color_to_play)
        if len(all_moves) == 0:
            return 'PAT'
        if len(all_moves) == 1:
            self.board = all_moves[0]
            self._color_to_play *= -1
            return

        for index, move in enumerate(all_moves):
            value = self.evaluate(move, depth, - self._color_to_play)
            if max_value is None or (self._color_to_play * value > self._color_to_play * max_value):
                max_value = value
                best_moves = [move]
            elif value == max_value:
                best_moves.append(move)
        print('board value '+str(max_value))
        self.board = random.choice(best_moves)
        self._color_to_play *= -1

    def evaluate(self, board, depth, color_to_play):
        if depth == 0:
            return board.value()
        max_ = - 9999
        min_ = 9999
        pat = True
        for b in board.possible_move(color_to_play):
            pat = False
            evaluation_b = self.evaluate(b, depth - 1, - color_to_play)
            min_ = min(min_, evaluation_b)
            max_ = max(max_, evaluation_b)

        if pat:
            return 0
        if color_to_play == 1:
            return max_
        return min_

    def print_board(self):
        self.printer.print_html(self.board)

    def print_history_board(self):
        self.printer.print_html(self.board, 'template/history.html', 'a')