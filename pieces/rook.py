from pieces.piece import Piece


class Rook(Piece):

    def __init__(self, color, position_x, position_y):
        Piece.__init__(self, color, position_x, position_y)

    def __repr__(self):
        return '\u265c' if self.color == 1 else '\u2656'

    def to_html(self):
        return '&#9814;' if self.color == 1 else '&#9820;'


    @property
    def value(self):
        return 5 * self.color

    def possible_moves(self, board):
        # TODO : To optimise by looping on delta_position
        possible_moves = []
        for x in range(self.position_x + 1, 8):
            # increasing x moves
            if self.is_partner(x, self.position_y, board):
                break
            possible_moves.append((x, self.position_y))
            if self.is_oponent(x, self.position_y, board):
                break

        for x in range(self.position_x - 1, -1, -1):
            # decreasing x moves
            if self.is_partner(x, self.position_y, board):
                break
            possible_moves.append((x, self.position_y))
            if self.is_oponent(x, self.position_y, board):
                break

        for y in range(self.position_y + 1, 8):
            if self.is_partner(self.position_x, y, board):
                break
            possible_moves.append((self.position_x, y))
            if self.is_oponent(self.position_x, y, board):
                break
        for y in range(self.position_y - 1, -1, -1):
            if self.is_partner(self.position_x, y, board):
                break
            possible_moves.append((self.position_x, y))
            if self.is_oponent(self.position_x, y, board):
                break
        return possible_moves


    def copy(self):
        return Rook(self.color, self.position_x, self.position_y)
