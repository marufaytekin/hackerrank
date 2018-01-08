"""
Write pow method without using built in pos function.
"""


def my_pow(a, b):
    """
    O(n)
    """
    if b < 0:
        a = 1.0 / a
        b = -b
    if b == 0:
        return 1
    else:
        return a * my_pow(a, b - 1)


def my_pow2(a, b):
    """
    O(lg(n))
    """
    if b < 0:
        a = 1.0 / a
        b = -b
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        if b % 2 == 0:
            half = my_pow2(a, b / 2)
            return half * half
        else:
            half = my_pow2(a, (b - 1) / 2)
            return a * half * half

assert pow(3, -1) == my_pow(3, -1)
assert pow(3, -1) == my_pow2(3, -1)
assert pow(3, 0) == my_pow(3, 0)
assert pow(3, 0) == my_pow2(3, 0)
assert pow(3, 2) == my_pow(3, 2)
assert pow(3, 2) == my_pow2(3, 2)
assert pow(2, 3) == my_pow(2, 3)
assert pow(2, 3) == my_pow2(2, 3)

assert pow(4, 4) == my_pow(4, 4)