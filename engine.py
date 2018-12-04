from pieces.rook import Rook
from board import Board


board = Board()
board.add_piece(Rook, 'w', 0, 0)

for index, possible_board in enumerate(board.possible_move('w')):
    print('board {}:\n{}'.format(index, possible_board))
