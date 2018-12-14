from unittest import TestCase
from tools.board_filler import BoardFiller

from pieces import Bishop, King, Knight, Pawn, Queen, Rook
from config import WHITE, BLACK


class TestBoardFiller(TestCase):

    def test_fill_from_text(self):
        board_filler = BoardFiller()
        board = board_filler.fill(text='rnbqk.../p......../......../......../......../......../P......./RNBQK...')
        self.assert_right_piece(board, 0, 0, Rook, WHITE)
        self.assert_right_piece(board, 1, 0, Knight, WHITE)
        self.assert_right_piece(board, 2, 0, Bishop, WHITE)
        self.assert_right_piece(board, 3, 0, Queen, WHITE)
        self.assert_right_piece(board, 4, 0, King, WHITE)
        self.assert_right_piece(board, 0, 1, Pawn, WHITE)
        self.assert_right_piece(board, 0, 7, Rook, BLACK)
        self.assert_right_piece(board, 1, 7, Knight, BLACK)
        self.assert_right_piece(board, 2, 7, Bishop, BLACK)
        self.assert_right_piece(board, 3, 7, Queen, BLACK)
        self.assert_right_piece(board, 4, 7, King, BLACK)
        self.assert_right_piece(board, 0, 6, Pawn, BLACK)

    def test_invalid_board(self):
        with self.assertRaises(Exception) as context:
            board_filler = BoardFiller()
            board_filler.fill(text='r')
        self.assertTrue(hasattr(context, 'exception'))

        with self.assertRaises(Exception) as context:
            board_filler = BoardFiller()
            board_filler.fill(text='Xnbqk.../p......../......../......../......../......../P......./RNBQK...')
        self.assertTrue(hasattr(context, 'exception'))

    def assert_right_piece(self, board, x, y, class_, color):
        piece = board[x][y]
        self.assertTrue(piece, msg='the board is empty in position x={} y={}'.format(x, y))
        self.assertTrue(
            isinstance(piece, class_),
            msg='the piece in position x={} y={} must be an instance of {}. {} found'.format(x, y, class_, type(piece))
        )
        self.assertEqual(piece.color, color)
