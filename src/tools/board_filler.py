from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from config import WHITE, BLACK
from board import Board


class BoardFiller:
    def __init__(self):
        self.char_mapping = {
            'P': Pawn,
            'R': Rook,
            'N': Knight,
            'B': Bishop,
            'Q': Queen,
            'K': King
        }

    def fill(self, text=None, file=None):
        """Fills a board from a textual representation
            :param
            - text (str)
                representation of the board
                defaults to None
            - file (str)
                file where the representation is written.
                used only if repr is None.
        """
        assert text or file, "text or file should be specified."
        if text:
            return self._fill_from_text(text)
        return self._fill_from_file(file)

    def _fill_from_text(self, text):
        self._check_valid_text(text)
        board = Board()
        for position_y, line in enumerate(text.split('/')):
            for position_x, char in enumerate(line):
                if char != '.':
                    color = WHITE if char.isupper() else BLACK
                    board.add_piece(
                        self.char_mapping[char.upper()],
                        color,
                        position_x,
                        7 - position_y
                    )
        return board

    def _fill_from_file(self, file):
        with open(file) as f:
            text = ''.join(f.readlines()).replace('\n', '/')
            return self._fill_from_text(text)

    def _check_valid_text(self, text):
        assert len(text.split('/')) == 8, \
            'The text representation {} must contain 8 series of 8 characters separated by a `/`'.format(text)
        for char in text:
            assert char.upper() in self.char_mapping or char in '/.', "Unknown character {}".format(char)
