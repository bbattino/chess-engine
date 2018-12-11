from copy import deepcopy
from pieces import Bishop, King, Knight, Pawn, Queen, Rook

import numpy as np

WHITE = 1
BLACK = -1


class Board:
    def __init__(self, method='legal', board=None):
        if board:
            self.board = board
        else:
            self.board = [[None for _ in range(8)] for _ in range(8)]
            if method == 'legal':
                self.legal_init_board()
            if method == 'exercice':
                self.exercice()
        self.possible_moves = {}
        self.last_move = None

    def __repr__(self):
        return '\n'.join(
            [
                ' '.join(
                    [
                        self.board[x][y].__repr__() if self.board[x][y] else '.'
                        for x in range(8)
                    ]
                )
                for y in range(8)
            ]
        )

    def __getitem__(self, x):
        return self.board[x]

    def __copy__(self):
        return Board(board=deepcopy(self.board))

    def add_piece(self, piece_class, color, x, y):
        self.board[x][y] = piece_class(color, x, y)

    def move_piece(self, x1, y1, x2, y2):
        self.last_move = x1, y1, x2, y2
        if self.is_promotion(x1, y1, x2, y2):
            return
        piece = self.board[x1][y1]
        piece.set_position(x2, y2)
        self.board[x2][y2] = piece
        self.board[x1][y1] = None

    def is_promotion(self, x1, y1, x2, y2):
        piece = self.board[x1][y1]
        if isinstance(piece, Pawn) and y2 in [0, 7]:
            self.board[x2][y2] = Queen(piece.color, x2, y2)
            self.board[x1][y1] = None
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
            piece = self.board[x][y]
            if piece and piece.color == color:
                moves = piece.possible_moves(self.board)
                if moves:
                    for move_x, move_y in moves:
                        if move_x != x or move_y != y:
                            board_copy = self.__copy__()
                            board_copy.move_piece(x, y, move_x, move_y)
                            self.possible_moves[color].append(board_copy)

    def value(self):
        value = 0
        for x, y in np.ndindex((8, 8)):
            piece = self.board[x][y]
            if piece:
                value += piece.value
        return value

    def exercice(self):
        for x in range(3):
            self.add_piece(Pawn, WHITE, x, 4)
            self.add_piece(Pawn, BLACK, x, 6)

        # self.add_piece(King, WHITE, 7, 0)
        # self.add_piece(King, BLACK, 7, 0)

    def legal_init_board(self):
        for x in range(8):
            self.add_piece(Pawn, WHITE, x, 1)
            self.add_piece(Pawn, BLACK, x, 6)

        self.add_piece(Rook, WHITE, 0, 0)
        self.add_piece(Rook, WHITE, 7, 0)
        self.add_piece(Rook, BLACK, 0, 7)
        self.add_piece(Rook, BLACK, 7, 7)

        self.add_piece(Knight, WHITE, 1, 0)
        self.add_piece(Knight, WHITE, 6, 0)
        self.add_piece(Knight, BLACK, 1, 7)
        self.add_piece(Knight, BLACK, 6, 7)

        self.add_piece(Bishop, WHITE, 2, 0)
        self.add_piece(Bishop, WHITE, 5, 0)
        self.add_piece(Bishop, BLACK, 2, 7)
        self.add_piece(Bishop, BLACK, 5, 7)

        self.add_piece(Queen, WHITE, 3, 0)
        self.add_piece(Queen, BLACK, 3, 7)
        self.add_piece(King, WHITE, 4, 0)
        self.add_piece(King, BLACK, 4, 7)

