"""
Given a numbers n, check if ynis a power of 10 or not.
"""


def power(n, d):
    if n == 1:
        return d
    if n % 10 != 0:
        return False
    if n < 1:
        return False
    return power(float(n)/10, d+1)


print(power(100, 0))
print(power(101, 0))
print(power(10, 0))
print(power(0, 0))
print(power(1000000, 0))
