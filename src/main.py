import time

from engine import Engine

engine = Engine()
engine.print_board()

for i in range(300):
    time.sleep(2)
    d = max(3, 9-i)
    t = time.time()
    engine.play(depth=0)
    print('time to play: {}\n'.format(time.time() - t), flush=True)
    engine.print_board()

