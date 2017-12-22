"""
Given the length and width of a board, also given a number n.
To generate a board that randomly contains n mines in this board.
"""
import random


def generate_board(l, w, n):
    board = []
    for i in range(l):
        line = []
        for j in range(w):
            line.append(0)
        board.append(line)
    for k in range(n):
        i = random.randint(0, l - 1)
        j = random.randint(0, w - 1)
        board[i][j] = 1
    return board


my_board = generate_board(7, 7, 15)

for line in my_board:
    print line
