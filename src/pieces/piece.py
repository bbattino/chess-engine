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

    @staticmethod
    def is_piece(x, y, board):
        return board[x][y]

    def is_opponent(self, x, y, board):
        return board[x][y] and board[x][y].color != self.color

    def is_partner(self, x, y, board):
        return board[x][y] and board[x][y].color == self.color

    @staticmethod
    def is_legal_move(x, y):
        return 0 <= x < 8 and 0 <= y < 8
