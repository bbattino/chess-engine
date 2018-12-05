from pieces import Bishop, King, Knight, Pawn, Queen, Rook

class Board:
    def __init__(self, method='legal'):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        if method == 'legal':
            self.legal_init_board()

    def __repr__(self):
        return '\n'.join(
            [
                ' '.join(
                    [
                        self.board[x][y].__repr__() if self.board[x][y] else '.'
                        for x in range(8)
                    ]
                )
                for y in range(8)
            ]
        )

    def __getitem__(self, x):
        return self.board[x]

    def __copy__(self):
        copy = Board()
        for x in range(8):
            for y in range(8):
                copy.board[x][y] = self.board[x][y].copy() if self.board[x][y] else None
        return copy

    def add_piece(self, piece_class, color, x, y):
        self.board[x][y] = piece_class(color, x, y)

    def move_piece(self, x1, y1, x2, y2):
        if self.is_promotion(x1, y1, x2, y2):
            return
        piece = self.board[x1][y1]
        piece.set_position(x2, y2)
        self.board[x2][y2] = piece
        self.board[x1][y1] = None

    def is_promotion(self, x1, y1, x2, y2):
        piece = self.board[x1][y1]
        if isinstance(piece, Pawn) and y2 in [0, 7]:
            self.board[x2][y2] = Queen(piece.color, x2, y2)
            self.board[x1][y1] = None
            return True
        return False


    def possible_move(self, color):
        boards = []
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if piece and piece.color == color:
                    moves = piece.possible_moves(self.board)
                    if moves:
                        for move_x, move_y in moves:
                            if move_x != x or move_y != y:
                                board_copy = self.__copy__()
                                board_copy.move_piece(x, y, move_x, move_y)
                                boards.append(board_copy)
        return boards

    def value(self):
        value = 0
        for x in range(8):
            for y in range(8):
                if self.board[x][y]:
                    value += self.board[x][y].value
        return value

    def legal_init_board(self):
        for x in range(8):
            self.add_piece(Pawn, True, x, 1)
            self.add_piece(Pawn, False, x, 6)

        self.add_piece(Rook, True, 0, 0)
        self.add_piece(Rook, True, 7, 0)
        self.add_piece(Rook, False, 0, 7)
        self.add_piece(Rook, False, 7, 7)

        self.add_piece(Knight, True, 1, 0)
        self.add_piece(Knight, True, 6, 0)
        self.add_piece(Knight, False, 1, 7)
        self.add_piece(Knight, False, 6, 7)

        self.add_piece(Bishop, True, 2, 0)
        self.add_piece(Bishop, True, 5, 0)
        self.add_piece(Bishop, False, 2, 7)
        self.add_piece(Bishop, False, 5, 7)

        self.add_piece(Queen, True, 3, 0)
        self.add_piece(Queen, False, 3, 7)
        self.add_piece(King, True, 4, 0)
        self.add_piece(King, False, 4, 7)
