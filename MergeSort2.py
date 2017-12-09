"""
MergeSort Algorithm:
1. Divide the list in two sides 
2. Sort left side
3. Sort Right side
4. Merge left and right
5. Repeat this in a recursive manner

Merge Function:
1. Use three index pointers as follows:
  i: index the first element in the left side
  j: index of the first element in the right side
  k: ndex of the first element in the auxiliary array
  mid: index to the middle element.
2. if i is exhausted than kth element = jth element
   if j is exhausted  than kth element = ith element
   if element[i] < element[j] than kth element = element[i]
   else kth element = element[j]
3. Return auxilary arr
"""

#
# def merge(a, low, mid, hi):
#     i = low
#     j = mid + 1
#     aux = []
#     for item in a:
#         aux.append(item)
#     for k in range(low, hi+1):
#         if i > mid:
#             a[k] = aux[j]
#             j += 1
#         elif j > hi:
#             a[k] = aux[i]
#             i += 1
#         elif a[i] < a[j]:
#             a[k] = aux[i]
#             i += 1
#         else:
#             a[k] = aux[j]
#             j += 1
#
#
# def sort(a, low, hi):
#     if low >= hi:
#         return
#     mid = low + (hi - low) / 2
#     sort(a, low, mid)
#     sort(a, mid + 1, hi)
#     merge(a, low, mid, hi)


def merge(a, b):
    '''
    merge two sorted lists     
    '''
    if a == None or b == None:
        return []
    n = len(a)
    m = len(b)
    res = (m+n) * [None]
    i = j = 0
    for k in range(n+m):
        if i >= n:
            res[k] = b[j]
            j += 1
        elif j >= m:
            res[k] = a[i]
            i += 1
        elif a[i] < b[j]:
            res[k] = a[i]
            i += 1
        else:
            res[k] = b[j]
            j += 1
    return res


def sort(a):
    if len(a) < 2:
        return a
    mid = len(a) / 2
    return merge(sort(a[0:mid]), sort(a[mid+1:len(a)]))


list1 = [3,4,7]
list2 = [1,2,3]

print merge(list1, list2)

sort(list1)
