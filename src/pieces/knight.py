from pieces.piece import Piece


class Knight(Piece):

    def __repr__(self):
        return '\u265e' if self.color == 1 else '\u2658'

    def to_html(self):
        return '&#9816;' if self.color == 1 else '&#9822;'

    @property
    def value(self):
        if self._value:
            return self._value
        self._value = 3 * self.color
        return self._value

    def possible_moves(self, board):
        # TODO : To optimise by looping on delta_position
        moves = [
            (self._position_x + sign_x * delta_x, self._position_y + sign_y * delta_y)
            for sign_x in [-1, 1]
            for sign_y in [-1, 1]
            for delta_x, delta_y in [(2, 1), (1, 2)]
        ]
        return [
            (move_x, move_y)
            for move_x, move_y in moves
            if self.is_legal_move(move_x, move_y) and not self.is_partner(move_x, move_y, board)
        ]

