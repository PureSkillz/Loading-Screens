import time
i = 0
red = 0
moves = ["◴", "◷", "◶", "◵"]


def roll(circle, times):
    print('\r', " " * times, circle, end='')
    time.sleep(0.25)


def spin(circle):
    print('\r', circle, end='')
    time.sleep(0.25)


while True:
    # roll(moves[red % 4], i)
    # spin(moves[red % 4])
    i += 1
    red += 1