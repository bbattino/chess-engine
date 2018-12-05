from engine import Engine
import time

engine = Engine()
engine.print_board()

for _ in range(30):
    engine.play()
    engine.print_board()
    time.sleep(2)
