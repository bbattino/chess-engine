from pieces.piece import Piece


class Pawn(Piece):

    def __init__(self, color, position_x, position_y):
        Piece.__init__(self, color, position_x, position_y)

    def __repr__(self):
        return '\u265f' if self.color == 1 else '\u2659'

    def to_html(self):
        return '&#9817;' if self.color == 1 else '&#9823;'

    @property
    def value(self):
        if self._value:
            return self._value
        if self.color == 1:
            self._value = 1 + (self._position_y - 1) / 14
        else:
            self._value = - 1 - (6 - self._position_y) / 14
        return self._value

    def possible_moves(self, board):
        # TODO add en passant capture
        # TODO handle promotion
        possible_moves = []
        y = self._position_y + self.color
        if not self.is_piece(self._position_x, y, board):
            possible_moves.append((self._position_x, y))
            if self.color == 1 and y == 2 and not self.is_piece(self._position_x, 3, board):
                possible_moves.append((self._position_x, 3))
            elif self.color == -1 and y == 5 and not self.is_piece(self._position_x, 4, board):
                possible_moves.append((self._position_x, 4))
        for x in [self._position_x - 1, self._position_x + 1]:
            if self.is_legal_move(x, y) and self.is_oponent(x, y, board):
                possible_moves.append((x, y))
        return possible_moves

    def copy(self):
        return Pawn(self.color, self._position_x, self._position_y)
