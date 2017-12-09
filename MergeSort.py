"""
Merge sort.
O( n log(n) )
"""


def merge(a, low, mid, hi):
    aux = []
    for item in a:
        aux.append(item)
    i = low
    j = mid + 1
    for k in range(low, hi + 1):
        print i, j
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            a[k] = aux[i]
            i += 1
        else:
            a[k] = aux[j]
            j += 1


def sort(a, low, hi):
    if hi <= low:
        return
    mid = low + (hi - low) / 2
    sort(a, low, mid)
    sort(a, mid + 1, hi)
    merge(a, low, mid, hi)


def merge_sort(a):
    low_idx = 0
    hi_idx = len(a) - 1
    return sort(a, low_idx, hi_idx)


l = [1, 4, 6, 8, 9, 2, 3, 0, 5, 4, 7, 11, -4]

a1 = [1, 3, 2, 5]

# print merge(a1, 0, 1, 3)

merge_sort(l)
print l
