"""
write a function that returns sum of the numbers up to n
"""


def sumto(n):
    """
    recursive
    """
    if n == 0:
        return 0
    else:
        return n + sumto(n - 1)


def sumto_tr(n):
    """
    tail recursive
    """
    def sum_acc(n, acc):
        if n == 0:
            return acc
        b = acc + n
        return sum_acc(n-1, b)

    return sum_acc(n, 0)

print(sumto(100))
print(sumto_tr(100))


