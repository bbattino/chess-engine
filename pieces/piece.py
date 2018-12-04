class Piece:

    def __init__(self, color, position_x, position_y):
        self.color = color
        self.position_x = position_x
        self.position_y = position_y

    def __repr__(self):
        return '{}?{}{}'.format(self.color, self.position_x, self.position_y)

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y

    def possible_moves(self, board):
        return []


    def copy(self):
        return Piece(self.color, self.position_x, self.position_y)
