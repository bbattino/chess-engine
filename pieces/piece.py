class Piece:

    def __init__(self, color, position_x, position_y):
        self.color = color
        self.position_x = position_x
        self.position_y = position_y

    def __repr__(self):
        return '{}?{}{}'.format(self.color, self.position_x, self.position_y)

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y

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
        return Piece(self.color, self.position_x, self.position_y)
