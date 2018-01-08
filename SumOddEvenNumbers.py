"""
Take array as argument and print sum of odd numbers and even numbers.
"""


def sum_numbers(arr):
    sum_even = 0
    sum_odd = 0
    for num in arr:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    print "Sum of Even Numbers: %d | Sum of Odd Numbers: %d" % (sum_even, sum_odd)


def sum_numbers_rec(arr, even, odd):
    """
    recursive
    """
    if not arr:
        print "Sum of even numbers: %d | Sum of odd numbers: %d" % (even, odd)
    else:
        if arr[0] % 2 == 0:
            even += arr[0]
            return sum_numbers_rec(arr[1:], even, odd)
        else:
            odd += arr[0]
            return sum_numbers_rec(arr[1:], even, odd)


l = [1, 2, 6, 7, -3, -5, -4, 0]

sum_numbers(l)
sum_numbers_rec(l, 0, 0)
