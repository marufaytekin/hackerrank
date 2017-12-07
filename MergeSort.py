def sort(a, low, hi):
    if low >= hi:
        return
    mid = (hi + low) / 2
    sort(a, low, mid)
    sort(a, mid + 1, hi)
    return merge(a, low, mid, hi)


def merge(a, low, mid, hi):
    temp = len(a) * [-1]
    i = low
    j = mid + 1
    # print low, mid, hi
    # print range(low, hi+1)
    for k in range(low, hi + 1):
        print i, j
        if i > mid:
            temp[k] = a[j]
            j += 1
        elif j > hi:
            temp[k] = a[i]
            i += 1
        elif a[i] < a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
    return temp


def merge_sort(a):
    return sort(a, 0, len(a)-1)


l = [1, 4, 6, 8, 9, 2, 3, 0, 7, 11, -4]

a1 = [1, 3, 4, 2, 5]

print merge(a1, 0, 2, 4)

print merge_sort(l)
