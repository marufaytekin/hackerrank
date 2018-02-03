"""
Given the length and width of a board, also given a number n.
To generate a board that randomly contains n mines in this board.
"""
import random


def generate_board(l, w, n):
    board = []
    for i in range(l):
        _line = []
        for j in range(w):
            _line.append(0)
        board.append(_line)
    cnt = 0
    while cnt < n:
        i = random.randint(0, l - 1)
        j = random.randint(0, w - 1)
        if board[i][j] is not 1:
            board[i][j] = 1
            cnt += 1
    return board


my_board = generate_board(3, 3, 4)

for line in my_board:
    print line
