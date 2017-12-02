def binary_search(L, left, right, k):
    if left > right:
        return False
    mid = (left + right) / 2
    if k < L[mid]:
        return binary_search(L, left, mid - 1, k)
    elif k > L[mid]:
        return binary_search(L, mid + 1, right, k)
    else:
        return L[mid]


L = []

for i in range(0, 100000):
    L.append(i)

print binary_search(L, 0, len(L) - 1, 19000)

def binary_length(length):
    if length == 0:
        return 1
    else:
        return 2 * binary_length(length - 1)

print(binary_length(9))