"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within
the 32-bit signed integer range. For the purpose of this problem, assume that
your function returns 0 when the reversed integer overflows.
"""


def reverse_num(n):
    """
    reverse an integer
    """
    a = 0
    sign = False
    if n < 0:
        sign = True
        n = -n
    while n >= 1:
        a = 10 * a + n % 10
        n /= 10
    if abs(a) > (2 ** 31 - 1):  # if overflow occurs for 32 bit integer
        return 0
    if sign:
        return -a
    return a


def reverse_str(s):
    """
    reverse a string
    """
    s2 = list(s)
    size = len(s2)
    r = []
    for i in range(size):
        r.append(s2[-(i + 1)])
    return ''.join(r)


def reverse_string_by_wor(s):
    """
    Reverse a string by word. For instance, given "The sky is blue",
    output "blue is sky The".
    """
    l = s.split(" ")
    l.reverse()
    return ' '.join(l)


print reverse_num(123)
print reverse_num(-123)
print reverse_num(-122342353)
print reverse_str("abcdefg")
print reverse_string_by_wor("The sky is blue")
