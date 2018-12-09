from template.constant import HTML, HTML_CASE

import numpy as np

class Printer:

    def print_html(self, board, file='template/index.html'):
        self.board = board
        self._build_html()
        self._update_html(file)

    def _build_html(self):
        self.html = HTML.format(
            board=''.join(
                [
                    HTML_CASE.format(
                        color=self._board_color(x, y),
                        value=self._piece_repr(x, y)
                    )
                    for x, y in np.ndindex((8, 8))
                ]
            )
        )

    def _update_html(self, file):
        with open(file, 'w') as f:
            f.write(self.html)

    @staticmethod
    def _board_color(x, y):
        return 'white' if (x + y) % 2 else 'black'

    def _piece_repr(self, x, y):
        piece = self.board[x][y]
        return repr(piece) if piece else ' '
