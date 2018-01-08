"""
write a function that returns sum of the number up to n
"""


def sumupto(n):
    if n == 0:
        return 0
    else:
        return n + sumupto(n-1)


def sumupto_tr(n):
    def sum_acc(n, acc):
        if n == 0:
            return acc
        b = acc + n
        return sum_acc(n-1, b)

    return sum_acc(n, 0)

print(sumupto(100))
print(sumupto_tr(100))


