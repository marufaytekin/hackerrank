"""
determine if given 4 coordinates are vertices of a square.

0,1   1,1

0,0   1,0

center = (A+B+C+D) / 4
(2, 2)/4 => (0.5, 0.5)
"""
import math


def distance(A, CP):
    x1, y1 = A
    x2, y2 = CP
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def is_square(A, B, C, D):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D
    Xcp = float(x1 + x2 + x3 + x4) / 4
    Ycp = float(y1 + y2 + y3 + y4) / 4
    CP = (Xcp, Ycp)
    return distance(A, CP) == distance(B, CP) == distance(C, CP) == distance(D, CP)


print is_square((0, 0), (0, 1), (1, 0), (1, 1))

print distance((1, 1), (0, 0))
