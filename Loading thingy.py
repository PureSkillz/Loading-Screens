import time

turn = 0
moves = ["/", "─", "\\", "|"]


def clear_wait(move):
    print('\r', move, end='')
    time.sleep(0.25)


while True:
    clear_wait(moves[turn % 4])
    turn += 1
