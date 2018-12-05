from pieces.piece import Piece


class Knight(Piece):

    def __init__(self, color, position_x, position_y):
        Piece.__init__(self, color, position_x, position_y)
        self.value = 3 * (2 * (color == 'w') - 1)

    def __repr__(self):
        return '{}k{}{}'.format(self.color, self.position_x, self.position_y)

    def possible_moves(self, board):
        # TODO : To optimise by looping on delta_position
        moves = [
            (self.position_x + sign_x * delta_x, self.position_y + sign_y * delta_y)
            for sign_x in [-1, 1]
            for sign_y in [-1, 1]
            for delta_x, delta_y in [(2, 1), (1, 2)]
        ]
        return [
            (move_x, move_y)
            for move_x, move_y in moves
            if self.is_legal_move(move_x, move_y) and not self.is_partner(move_x, move_y, board)
        ]

    def copy(self):
        return Knight(self.color, self.position_x, self.position_y)
