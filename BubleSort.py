"""
implementation of bubble sort algorithm
"""
from Swap import swap


def bubble_sort(a):
    total_swaps = 0
    while True:
        swap_cnt = 0
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                swap(a, i, i + 1)
                swap_cnt += 1
                total_swaps += 1
        if swap_cnt == 0:
            break
    return total_swaps


l = [1, 2, 6, 3, 4, 7, -3, 9, 8, 5]

print(l)

num_swaps = bubble_sort(l)

print ("Array is sorted in {} swaps.".format(num_swaps))
print ("First Element: {}".format(l[0]))
print ("Last Element: {}".format(l[-1]))

