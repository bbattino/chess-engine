from pieces.piece import Piece


class King(Piece):
    def __repr__(self):
        return '\u265a' if self.color == 1 else '\u2654'

    def to_html(self):
        return '&#9812;' if self.color == 1 else '&#9818;'

    @property
    def value(self):
        if self._value:
            return self._value
        self._value = 1000 * self.color
        return self._value

    def possible_moves(self, board):
        deltas = list(set([
                              (sign_x * bool_x, sign_y * bool_y)
                              for sign_x in [-1, 1]
                              for sign_y in [-1, 1]
                              for bool_x in [1, 0]
                              for bool_y in [1, 0]
                              ]))
        return [
            (self._position_x + delta_x, self._position_y + delta_y)
            for delta_x, delta_y in deltas
            if self._is_valid_move(self._position_x + delta_x, self._position_y + delta_y, board)
            ]

    def _is_valid_move(self, x, y, board):
        return self.is_legal_move(x, y) and not self.is_partner(x, y, board)
