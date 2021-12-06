import time
i = 0
turn = 0
moves = ["△", "▷", "▽", "◁"]


def clear_wait(triangle, times):
    print('\r', " " * times, triangle, end='')
    time.sleep(0.33)


while True:
    clear_wait(moves[red % 4], i)
    i += 1
    turn += 1
