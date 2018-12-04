from pieces.piece import Piece


class Rook(Piece):

    def __init__(self, color, position_x, position_y):
        Piece.__init__(self, 'rook', color, position_x, position_y)

    def __repr__(self):
        return '{}R{}{}'.format(self.color, self.position_x, self.position_y)

    def possible_moves(self):
        return [
            (x, self.position_y)
            for x in range(8)
        ] + [
            (self.position_x, y)
            for y in range(8)
        ]

    def copy(self):
        return Rook(self.color, self.position_x, self.position_y)