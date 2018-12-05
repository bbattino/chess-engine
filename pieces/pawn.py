from pieces.piece import Piece


class Pawn(Piece):

    def __init__(self, color, position_x, position_y):
        Piece.__init__(self, color, position_x, position_y)
        self.value = 2 * (color == 'w') - 1


    def __repr__(self):
        return '{}P{}{}'.format(self.color, self.position_x, self.position_y)

    def possible_moves(self, board):
        # TODO add en passant capture
        # TODO handle promotion
        possible_moves = []
        y = self.position_y - 1 + 2 * (self.color == 'w')
        if not board[self.position_x][y]:
            possible_moves.append((self.position_x, y))
        for x in [self.position_x - 1, self.position_x + 1]:
            if self.is_legal_move(x, y) and not self.is_partner(x, y, board):
                possible_moves.append((x, y))
        return possible_moves

    def copy(self):
        return Pawn(self.color, self.position_x, self.position_y)
