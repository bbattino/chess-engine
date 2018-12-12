import numpy as np

from template.constant import HTML, HTML_CASE, BLANK_LINE, REPLACE_LINE


class Printer:

    def print_html(self, board, file='template/index.html', method='w'):
        self.board = board
        self._build_html(method)
        self._update_html(file)

    def _build_html(self, method):
        board = ''.join(
                [
                    HTML_CASE.format(
                        color=self._board_color(x, y, self.board),
                        value=self._piece_repr(x, y)
                    )
                    for x, y in np.ndindex((8, 8))
                ])
        if method == 'w' or not hasattr(self, 'html'):
            self.html = HTML.format(board=board)

        elif method == 'a':
            self.html = self.html.replace(BLANK_LINE, REPLACE_LINE.format(board=board))

    def _update_html(self, file):
        with open(file, 'w') as f:
            f.write(self.html)

    @staticmethod
    def _board_color(x, y, board):
        if board.last_move:
            x1, y1, x2, y2 = board.last_move
            if (x == x1 and y == y1) or (x == x2 and y == y2):
                return 'green'
        return 'white' if (x + y) % 2 else 'black'

    def _piece_repr(self, x, y):
        piece = self.board[x][y]
        return piece.to_html() if piece else ' '
