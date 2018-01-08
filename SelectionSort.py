"""
Selection Sort:
Start index i from 0 and go up to n-1 where n is the size of array follow the 
following steps:
1. find the smallest element in the the right side of the index i
2. swap the smallest element with the element in index i
3. increment i
4. go to step 1 and repeat until i = n
"""

from Swap import swap


def sort(l):
    """
    O(n^2)
    """
    n = len(l)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if l[j] < l[min_idx]:
                min_idx = j
        swap(l, i, min_idx)

l = [4, 9, 2, 1, 6, 8, 7, 4, 0]

sort(l)
print l
