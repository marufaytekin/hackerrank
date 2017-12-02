def sumupto(n):

    def sum_acc(n, acc):
        if n == 0:
            return acc
        b = acc + n
        return sum_acc(n-1, b)

    return sum_acc(n, 0)

print(sumupto(100))


