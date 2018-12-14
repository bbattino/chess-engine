from unittest import TestCase
from board import Board
from pieces import Bishop, King, Knight, Pawn, Queen, Rook


class TestMoves(TestCase):
    def test_bishop(self):
        board = Board(method='empty')
        board.add_piece(Bishop, 1, 3, 3)
        board.add_piece(Bishop, -1, 4, 4)

        all_moves_computed = [
            move.pgn
            for move in board.possible_move(1)
            ]
        all_true_moves = [
            ' d4 {};'.format(position)
            for position in ['e3', 'f2', 'g1', 'c5', 'b6', 'a7', 'c3', 'b2', 'a1']
            ]

        self.assertListEqual(all_moves_computed, all_true_moves)

    def test_king(self):
        board = Board(method='empty')
        board.add_piece(King, 1, 3, 3)

        all_moves_computed = [
            move.pgn
            for move in board.possible_move(1)
            ]
        all_true_moves = [
            ' d4 {};'.format(position)
            for position in ['d5', 'c5', 'c4', 'c3', 'd3', 'e4', 'e3', 'e5']
            ]

        self.assertListEqual(all_moves_computed, all_true_moves)

    def test_knight(self):
        board = Board(method='empty')
        board.add_piece(Knight, 1, 3, 3)

        all_moves_computed = [
            move.pgn
            for move in board.possible_move(1)
            ]
        all_true_moves = [
            ' d4 {};'.format(position)
            for position in ['b3', 'c2', 'b5', 'c6', 'f3', 'e2', 'f5', 'e6']
            ]

        self.assertListEqual(all_moves_computed, all_true_moves)

    def test_pawn(self):
        board = Board(method='empty')
        board.add_piece(Pawn, 1, 3, 3)
        board.add_piece(Pawn, -1, 4, 4)

        all_moves_computed = [
            move.pgn
            for move in board.possible_move(1)
            ]
        all_true_moves = [
            ' d4 {};'.format(position)
            for position in ['d5', 'e5']
            ]

        self.assertListEqual(all_moves_computed, all_true_moves)

    def test_rook(self):
        board = Board(method='empty')
        board.add_piece(Rook, 1, 3, 3)
        board.add_piece(Pawn, -1, 5, 3)

        all_moves_computed = [
            move.pgn
            for move in board.possible_move(1)
            ]
        all_true_moves = [
            ' d4 {};'.format(position)
            for position in ['e4', 'f4', 'c4', 'b4', 'a4', 'd5', 'd6', 'd7', 'd8', 'd3', 'd2', 'd1']
            ]

        self.assertListEqual(all_moves_computed, all_true_moves)
