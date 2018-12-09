from pieces.piece import Piece
from pieces import Rook, Bishop


class Queen(Piece):

    def __init__(self, color, position_x, position_y):
        Piece.__init__(self, color, position_x, position_y)

    def __repr__(self):
        # return '\u265b' if self.color else '\u2655'
        return '&#9813;' if self.color else '&#9819;'

    @property
    def value(self):
        return 8 * self.color

    def possible_moves(self, board):
        return list(set(Rook(
            self.color, self.position_x, self.position_y
        ).possible_moves(board) + Bishop(
            self.color, self.position_x, self.position_y
        ).possible_moves(board)))

    def copy(self):
        return Queen(self.color, self.position_x, self.position_y)
