from pieces import Rook, Pawn, Bishop, Knight, King
from board import Board


board = Board()

for x in range(8):
    board.add_piece(Pawn, 'w', x, 1)
    board.add_piece(Pawn, 'b', x, 6)

board.add_piece(Rook, 'w', 0, 0)
board.add_piece(Rook, 'w', 7, 0)
board.add_piece(Rook, 'b', 0, 7)
board.add_piece(Rook, 'b', 7, 7)

board.add_piece(Knight, 'w', 1, 0)
board.add_piece(Knight, 'w', 6, 0)
board.add_piece(Knight, 'b', 1, 7)
board.add_piece(Knight, 'b', 6, 7)

board.add_piece(Bishop, 'w', 2, 0)
board.add_piece(Bishop, 'w', 5, 0)
board.add_piece(Bishop, 'b', 2, 7)
board.add_piece(Bishop, 'b', 5, 7)

board.add_piece(King, 'w', 4, 0)
board.add_piece(King, 'b', 4, 7)


for index, possible_board in enumerate(board.possible_move('w')):
    print('board {}:\n{}'.format(index, possible_board))
