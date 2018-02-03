import random
from Swap import swap


def shuffle(in_list):
    n = len(in_list)
    for i in range(1, n):
        j = random.randint(0, i - 1)
        swap(in_list, i, j)
    return in_list


l = [1, 9, 3, 5, 7, 0, -3, 2, 3, 4]

print shuffle(l)
