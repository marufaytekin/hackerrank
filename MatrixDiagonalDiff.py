"""
You have an nxn matrix of numbers. You need to find the sum  of the two diagonals
and output the absolute value of the difference. For instance if you have
[ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
then output abs((1+5+9)-(3+5+7))
"""


def diagonal_diff(mat):
    n = len(mat)
    diag_1 = 0
    diag_2 = 0
    for i in range(n):
        diag_1 += mat[i][i]
        diag_2 += mat[i][n - i - 1]
    return abs(diag_1 - diag_2)


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print diagonal_diff(m)
