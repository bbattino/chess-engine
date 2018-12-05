from pieces.piece import Piece


class King(Piece):

    def __init__(self, color, position_x, position_y):
        Piece.__init__(self, color, position_x, position_y)
        self.value = 1000 * (2 * color - 1)


    def __repr__(self):
        return '&#9812;' if self.color else '&#9818;'
        # return '\u265a' if self.color else '\u2654'

    def possible_moves(self, board):
        deltas = list(set([
            (sign_x * bool_x, sign_y * bool_y)
            for sign_x in [-1, 1]
            for sign_y in [-1, 1]
            for bool_x in [1, 0]
            for bool_y in [1, 0]
        ]))
        return [
            (self.position_x + delta_x, self.position_y + delta_y)
            for delta_x, delta_y in deltas
            if self._is_valid_move(self.position_x + delta_x, self.position_y + delta_y, board)
        ]

    def copy(self):
        return King(self.color, self.position_x, self.position_y)

    def _is_valid_move(self, x, y, board):
        return self.is_legal_move(x, y) and not self.is_partner(x, y, board)
