import time

from engine import Engine

'''
from _board import Board
from tools.printer import Printer
b = Board()
index = 0
p = Printer()
all_moves = b.possible_move(True)
for i, move in enumerate(all_moves):
    p.print_html(move, 'template/{}.html'.format(i))

print(len(all_moves))
# for move1 in all_moves:
    #moves1 = move1.possible_move(False)
    #for move in moves1:
    #   move2 = move.possible_move(True)
    # index +=1
'''
engine = Engine()
engine.print_board()

for i in range(300):
    # time.sleep(2)
    d = max(3, 9-i)
    t = time.time()
    engine.play(deapth=0)
    print(time.time() - t, flush=True)
    engine.print_board()

