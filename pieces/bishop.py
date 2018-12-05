from pieces.piece import Piece


class Bishop(Piece):

    def __init__(self, color, position_x, position_y):
        Piece.__init__(self, color, position_x, position_y)

    def __repr__(self):
        return '{}b{}{}'.format(self.color, self.position_x, self.position_y)

    def possible_moves(self, board):
        deltas = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        possible_moves = []
        for delta_x, delta_y in deltas:
            for length in range(1, 8):
                x = self.position_x + length * delta_x
                y = self.position_y + length * delta_y
                if not self._is_valid_move(x, y, board):
                    break
                possible_moves.append((x, y))
                if self._is_capture(x, y, board):
                    break
        return possible_moves


    def copy(self):
        return Bishop(self.color, self.position_x, self.position_y)

    def _is_valid_move(self, x, y, board):
        return self.is_legal_move(x, y) and not self.is_piece(x, y, board)

    def _is_capture(self, x, y, board):
        return board[x][y] and board[x][y].color != self.color
