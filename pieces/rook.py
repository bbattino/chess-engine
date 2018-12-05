from pieces.piece import Piece


class Rook(Piece):

    def __init__(self, color, position_x, position_y):
        Piece.__init__(self, color, position_x, position_y)
        self.value = 5 * (2 * (color == 'w') - 1)


    def __repr__(self):
        return '{}R{}{}'.format(self.color, self.position_x, self.position_y)

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
