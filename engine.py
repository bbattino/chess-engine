from board import Board
from tools.printer import Printer

import random
import time


class Engine:
    def __init__(self):
        self.board = Board(method='exercice')
        self.printer = Printer()
        self._white_to_play = True

    def play(self, method='value', deapth=11):
        if method == 'random':
            self.random_play()
        elif method == 'value':
            self.play_value(deapth)

    def random_play(self):
        self.board = random.choice(self.board.possible_move(self._white_to_play))
        self._white_to_play = 1 - self._white_to_play

    def play_value(self, depth):
        max_value = None
        best_moves = []
        coefficient = 1 if self._white_to_play else -1
        all_moves = self.board.possible_move(self._white_to_play)
        if len(all_moves) == 0:
            return 'PAT'
        for index, move in enumerate(all_moves):
            value = self.evaluate(move, depth, not self._white_to_play)
            if max_value is None or (coefficient * value > coefficient * max_value):
                max_value = value
                best_moves = [move]
            elif value == max_value:
                best_moves.append(move)
        print('board value '+str(max_value))
        self.board = random.choice(best_moves)
        self._white_to_play = 1 - self._white_to_play

    def evaluate(self, board, depth, is_white_playing):
        if depth == 0:
            return board.value()
        '''
        all_evaluations = []
        for b in board.possible_move(is_white_playing):

            all_evaluations.append(self.evaluate(b, depth - 1, not is_white_playing))
        '''
        all_evaluations = [
            self.evaluate(b, depth-1, not is_white_playing)
            for b in board.possible_move(is_white_playing)
        ]
        if len(all_evaluations) == 0:
            return 0
        if is_white_playing:
            return max(all_evaluations)
        return min(all_evaluations)

    def print_board(self):
        self.printer.print_html(self.board)
