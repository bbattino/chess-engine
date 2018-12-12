from pieces import Rook, Bishop, Piece


class Queen(Piece):

    def __init__(self, color, position_x, position_y):
        Piece.__init__(self, color, position_x, position_y)

    def __repr__(self):
        return '\u265b' if self.color == 1 else '\u2655'

    def to_html(self):
        return '&#9813;' if self.color == 1 else '&#9819;'


    @property
    def value(self):
        if self._value:
            return self._value
        self._value = 8 * self.color
        return self._value

    def possible_moves(self, board):
        return list(set(Rook(
            self.color, self._position_x, self._position_y
        ).possible_moves(board) + Bishop(
            self.color, self._position_x, self._position_y
        ).possible_moves(board)))

    def copy(self):
        return Queen(self.color, self._position_x, self._position_y)
