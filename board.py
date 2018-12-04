class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def __repr__(self):
        return '\n'.join(
            [
                ' '.join(
                    [
                        self.board[x][y].__repr__() if self.board[x][y] else '....'
                        for x in range(8)
                    ]
                )
                for y in range(8)
            ]
        )

    def __copy__(self):
        copy = Board()
        for x in range(8):
            for y in range(8):
                copy.board[x][y] = self.board[x][y].copy() if self.board[x][y] else None
        return copy

    def add_piece(self, piece_class, color, x, y):
        self.board[x][y] = piece_class(color, x, y)

    def move_piece(self, x1, y1, x2, y2):
        piece = self.board[x1][y1]
        piece.set_position(x2, y2)
        self.board[x2][y2] = piece
        self.board[x1][y1] = None

    def possible_move(self, color):
        boards = []
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if piece and piece.color == color:
                    moves = piece.possible_moves()
                    if moves:
                        for move_x, move_y in moves:
                            if move_x != x or move_y != y:
                                board_copy = self.__copy__()
                                board_copy.move_piece(x, y, move_x, move_y)
                                boards.append(board_copy)
        return boards

