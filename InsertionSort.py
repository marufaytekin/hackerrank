"""
Insertion Sort
Use index i from 0 to n-1 to process all elements of an array where
n is the size of the array
Everyting on the left side of i is going to be sorted.
1. select element[i]
2. move element i to the left until it is in correct place
3. increment i and repeat.
"""

from swap import swap


def sort(l):
    n = len(l)
    for i in range(n):
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                swap(l, j, j-1)

my_list = [4, 9, 2, 0, 1, 3, 4, 6, 5]

sort(my_list)
print my_list



