from copy import deepcopy

import numpy as np

from pieces import Pawn, Queen


class Board:
    def __init__(self, board=None, pgn=None):
        self._board = board or np.full((8, 8), False, dtype=object)
        self.possible_moves = {}
        self.last_move = None
        self.pgn = pgn or ''

    def __repr__(self):
        return '\n'.join(
            [
                ' '.join(
                    [
                        repr(self._board[x][y]) if self._board[x][y] else '.'
                        for x in range(8)
                    ]
                )
                for y in range(8)
            ]
        )

    def __getitem__(self, x):
        return self._board[x]

    def __copy__(self):
        return Board(board=deepcopy(self._board), pgn=self.pgn)

    def add_piece(self, piece_class, color, x, y):
        self._board[x][y] = piece_class(color, x, y)

    def set_board(self, board):
        self._board = board

    def move_piece(self, x1, y1, x2, y2):
        self.last_move = x1, y1, x2, y2
        if self.is_promotion(x1, y1, x2, y2):
            return
        self.pgn += ' {}{} {}{};'.format(
            chr(ord('a') + x1),
            y1 + 1,
            chr(ord('a') + x2),
            y2 + 1
        )
        piece = self._board[x1][y1]
        piece.set_position(x2, y2)
        self._board[x2][y2] = piece
        self._board[x1][y1] = None

    def is_promotion(self, x1, y1, x2, y2):
        piece = self._board[x1][y1]
        if isinstance(piece, Pawn) and y2 in [0, 7]:
            self._board[x2][y2] = Queen(piece.color, x2, y2)
            self._board[x1][y1] = False
            return True
        return False

    def possible_move(self, color):
        if color in self.possible_moves:
            return self.possible_moves[color]
        self.compute_possible_move(color)
        return self.possible_moves[color]

    def compute_possible_move(self, color):
        self.possible_moves[color] = []
        for x, y in np.ndindex((8, 8)):
            piece = self._board[x][y]
            if piece and piece.color == color:
                moves = piece.possible_moves(self._board)
                if moves:
                    for move_x, move_y in moves:
                        if move_x != x or move_y != y:
                            board_copy = self.__copy__()
                            board_copy.move_piece(x, y, move_x, move_y)
                            self.possible_moves[color].append(board_copy)

    def value(self):
        value = 0
        for x, y in np.ndindex((8, 8)):
            piece = self._board[x][y]
            if piece:
                value += piece.value
        return value
