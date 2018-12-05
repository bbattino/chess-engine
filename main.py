from engine import Engine

engine = Engine()
engine.print_board()

for _ in range(30):
    engine.play()
    engine.print_board()
