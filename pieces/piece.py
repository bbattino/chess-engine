class Piece:

    def __init__(self, name, color, position_x, position_y):
        self.name = name
        self.color = color
        self.position_x = position_x
        self.position_y = position_y

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y


    def move(self):
        ...
