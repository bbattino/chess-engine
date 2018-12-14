from pieces.piece import Piece


class Rook(Piece):
    def __repr__(self):
        # TODO White
        return '\u265c' if self.color == 1 else '\u2656'

    def to_html(self):
        return '&#9814;' if self.color == 1 else '&#9820;'

    @property
    def value(self):
        if self._value:
            return self._value
        self._value = 5 * self.color
        return self._value

    def possible_moves(self, board):
        # TODO : To optimise by looping on delta_position
        possible_moves = []
        for x in range(self._position_x + 1, 8):
            # increasing x moves
            if self.is_partner(x, self._position_y, board):
                break
            possible_moves.append((x, self._position_y))
            if self.is_opponent(x, self._position_y, board):
                break

        for x in range(self._position_x - 1, -1, -1):
            # decreasing x moves
            if self.is_partner(x, self._position_y, board):
                break
            possible_moves.append((x, self._position_y))
            if self.is_opponent(x, self._position_y, board):
                break

        for y in range(self._position_y + 1, 8):
            if self.is_partner(self._position_x, y, board):
                break
            possible_moves.append((self._position_x, y))
            if self.is_opponent(self._position_x, y, board):
                break
        for y in range(self._position_y - 1, -1, -1):
            if self.is_partner(self._position_x, y, board):
                break
            possible_moves.append((self._position_x, y))
            if self.is_opponent(self._position_x, y, board):
                break
        return possible_moves
