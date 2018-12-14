import random

from board import Board
from config import WHITE
from tools.printer import Printer
from tools.board_filler import BoardFiller


class Engine:
    def __init__(self):
        self._board = Board()
        self._standard_match_init_board()
        self.printer = Printer()
        self._color_to_play = WHITE

    def play(self, method='value', depth=3):
        if method == 'random':
            self.random_play()
        elif method == 'value':
            self.play_value(depth)

    def random_play(self):
        self._board = random.choice(self._board.possible_move(self._color_to_play))
        self._color_to_play *= -1

    def play_value(self, depth):
        max_value = None
        best_moves = []
        all_moves = self._board.possible_move(self._color_to_play)
        if len(all_moves) == 0:
            return 'PAT'
        if len(all_moves) == 1:
            self._board = all_moves[0]
            self._color_to_play *= -1
            return

        for index, move in enumerate(all_moves):
            value = self.evaluate(move, depth, - self._color_to_play)
            if max_value is None or (self._color_to_play * value > self._color_to_play * max_value):
                max_value = value
                best_moves = [move]
            elif value == max_value:
                best_moves.append(move)
        self._board = random.choice(best_moves)
        print('move: {}\nvalue: {} '.format(self._board.pgn, max_value))
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
        self.printer.print_html(self._board)

    def print_history_board(self):
        self.printer.print_html(self._board, 'template/history.html', 'a')

    def _standard_match_init_board(self):
        self._board.set_board(
            BoardFiller().fill(text='rnbqkbnr/pppppppp/......../......../......../......../PPPPPPPP/RNBQKBNR')
        )


