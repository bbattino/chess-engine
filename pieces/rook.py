from pieces.piece import Piece


class Rook(Piece):

    def __init__(self, color, position_x, position_y):
        Piece.__init__(self, color, position_x, position_y)

    def __repr__(self):
        return '{}R{}{}'.format(self.color, self.position_x, self.position_y)

    def possible_moves(self, board):
        # TODO : To optimise by looping on delta_position
        possible_moves = []
        for x in range(self.position_x + 1, 8):
            # increasing x moves
            piece = board[x][self.position_y]
            if piece:
                if piece.color != self.color:
                    possible_moves.append((x, self.position_y))
                break
            possible_moves.append((x, self.position_y))

        for x in range(self.position_x - 1, -1, -1):
            # decreasing x moves
            piece = board[x][self.position_y]
            if piece:
                if piece.color != self.color:
                    possible_moves.append((x, self.position_y))
                break
            possible_moves.append((x, self.position_y))

        for y in range(self.position_y + 1, 8):
            piece = board[self.position_x][y]
            if piece:
                if piece.color != self.color:
                    possible_moves.append((self.position_x, y))
                break
            possible_moves.append((x, self.position_y))
        for y in range(self.position_y - 1, -1, -1):
            piece = board[self.position_x][y]
            if piece and piece.color == self.color:
                break
            possible_moves.append((self.position_x, y))
        return possible_moves


    def copy(self):
        return Rook(self.color, self.position_x, self.position_y)