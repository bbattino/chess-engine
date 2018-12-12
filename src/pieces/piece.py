class Piece:

    def __init__(self, color, position_x, position_y):
        self.color = color
        self._position_x = position_x
        self._position_y = position_y
        self._value = None

    def __repr__(self):
        return '?'

    def set_position(self, x, y):
        self._position_x = x
        self._position_y = y
        self._value = None

    @property
    def value(self):
        return self._value

    def possible_moves(self, board):
        return []

    def is_piece(self, x, y, board):
        return board[x][y] is not None

    def is_oponent(self, x, y, board):
        return board[x][y] and board[x][y].color != self.color

    def is_partner(self, x, y, board):
        return board[x][y] and board[x][y].color == self.color

    def is_legal_move(self, x, y):
        return 0 <= x < 8 and 0 <= y <8

    def copy(self):
        return Piece(self.color, self._position_x, self._position_y)
