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


def merge(left, right):
    """
    merge two sorted lists     
    """
    if left is None or right is None:
        return left or right
    n = len(left)
    m = len(right)
    # res = (m + n) * [None] // array version implementation
    res = []
    i = j = 0
    for k in range(n + m):
        if i >= n:
            # res[k] = right[j]
            res.append(right[j])
            j += 1
        elif j >= m:
            # res[k] = left[i]
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            # res[k] = left[i]
            res.append(left[i])
            i += 1
        else:
            # res[k] = right[j]
            res.append(right[j])
            j += 1
    return res


def sort(my_list):
    if len(my_list) < 2:
        return my_list
    mid = len(my_list) / 2
    left = sort(sort(my_list[:mid]))
    right = sort(my_list[mid:])
    return merge(left, right)


list1 = [3, 4, 7]
list2 = [1, 2, 3]
merge_res = [1, 2, 3, 3, 4, 7]
assert merge(list1, list2) == merge_res
assert merge(None, [1]) == [1]
assert merge([2], None) == [2]

l = [0, -1, 9, 4, 2, 3, 100, -344, 56, 23]
out = [-344, -1, 0, 2, 3, 4, 9, 23, 56, 100]
sorted_list = sort(l)
print (sorted_list)
assert sorted_list == out
