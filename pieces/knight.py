from pieces.piece import Piece


class Knight(Piece):

    def __init__(self, color, position_x, position_y):
        Piece.__init__(self, color, position_x, position_y)

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
            if 0 <= move_x < 8 and 0 <= move_y < 8 and (not board[move_x][move_y] or board[move_x][move_y].color != self.color)
        ]

    def copy(self):
        return Knight(self.color, self.position_x, self.position_y)