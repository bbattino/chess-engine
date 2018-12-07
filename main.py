from engine import Engine
import time

engine = Engine()
engine.print_board()

for _ in range(30):
    # time.sleep(2)
    engine.play()
    engine.print_board()
