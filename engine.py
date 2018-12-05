from pieces import Rook, Pawn, Bishop, Knight, King, Queen
from board import Board

import curses
import random
import time


board = Board()

is_playing = 'b'
boards = [board]
for _ in range(30):
    is_playing = 'w' if is_playing == 'b' else 'b'
    boards.append(
        random.choice(
            boards[-1].possible_move(is_playing)
        )
    )

def print_board(board, index):
    """progress: 0-10"""
    time.sleep(1.5)
    stdscr.addstr(0, 0, 'move {} : value {}'.format(index, board.value()))
    for i, line in enumerate(repr(board).split('\n')):
        stdscr.addstr(i + 1, 0, line)
    stdscr.refresh()

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

for index, b in enumerate(boards):
    print_board(b, index)
