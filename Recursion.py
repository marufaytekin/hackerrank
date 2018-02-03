# coding=utf-8
""" 1. Write a function triangular_sum(num) that computes the arithmetic sum 0+1+2...+(num−1)+num.
For example, triangular_sum(3) should return 𝟼.
Note that this sum can be computed directly via a simple arithmetic formula,
but use a recursive approach instead."""


def triangular_sum(num):
    """
    recursive
    """
    if num == 0:
        return 0
    return num + triangular_sum(num - 1)


print(triangular_sum(3))


def triangular_sum_tr(num):
    """
    tail recursive
    """
    def triangular_sum_acc(a, acc):
        if a == 0:
            return acc
        else:
            acc += a
            return triangular_sum_acc(a - 1, acc)

    return triangular_sum_acc(num, 0)


print(triangular_sum_tr(3))

""" 2. Write a function 𝚗𝚞𝚖𝚋𝚎𝚛_𝚘𝚏_𝚝𝚑𝚛𝚎𝚎𝚜(𝚗𝚞𝚖) that returns the number of times the digit 𝟹 appears in
the decimal representation of the non-negative integer 𝚗𝚞𝚖. For example 𝚗𝚞𝚖𝚋𝚎𝚛_𝚘𝚏_𝚝𝚑𝚛𝚎𝚎𝚜(𝟹𝟺𝟻𝟹𝟺)
should return 𝟸. Solution """


def number_of_threes(num):
    """
    Recursive
    """
    if num == 0:
        return 0
    digit = num % 10
    if digit == 3:
        return 1 + number_of_threes(num / 10)
    else:
        return number_of_threes(num / 10)


print(number_of_threes(34534))


def number_of_threes_tr(num):
    """
    Tail recursive
    """

    def number_of_threes_acc(num_sub, acc):
        if num_sub == 0:
            return acc
        if num_sub % 10 == 3:
            acc += 1
        return number_of_threes_acc(num_sub / 10, acc)

    return number_of_threes_acc(num, 0)


print(number_of_threes_tr(34534))

""" 3. Write a function 𝚒𝚜_𝚖𝚎𝚖𝚋𝚎𝚛(𝚖𝚢_𝚕𝚒𝚜𝚝, 𝚎𝚕𝚎𝚖) that returns 𝚃𝚛𝚞𝚎 if 𝚎𝚕𝚎𝚖 is a member of
𝚖𝚢_𝚕𝚒𝚜𝚝 and 𝙵𝚊𝚕𝚜𝚎 otherwise. For example, 𝚒𝚜_𝚖𝚎𝚖𝚋𝚎𝚛(['𝚌', '𝚊', '𝚝'], '𝚊') should return
𝚃𝚛𝚞𝚎. Do not use any of Python's built-in list methods or an operator like 𝚒𝚗. """


def is_member(my_list, elem):
    if len(my_list) == 0:
        return False
    if my_list[0] == elem:
        return True
    return is_member(my_list[1:], elem)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print is_member(l, 1)
print is_member(l, 9)
print is_member(l, -1)
print is_member(l, 5)
print is_member(['𝚌', '𝚊', '𝚝'], '𝚊')

""" 4. Write a function 𝚛𝚎𝚖𝚘𝚟𝚎_𝚡(𝚖𝚢_𝚜𝚝𝚛𝚒𝚗𝚐) that takes the string 𝚖𝚢_𝚜𝚝𝚛𝚒𝚗𝚐 and deletes all
occurrences of the character '𝚡' from this string. For example, 𝚛𝚎𝚖𝚘𝚟𝚎_𝚡("𝚌𝚊𝚝𝚡𝚡𝚍𝚘𝚐𝚡") should return
"𝚌𝚊𝚝𝚍𝚘𝚐". You should not use Python's built-in string methods. """


def remove_x(my_string):
    """
    recursive
    """
    if my_string == "":
        return ""
    if my_string[0] == 'x':
        return remove_x(my_string[1:])
    else:
        return my_string[0] + remove_x(my_string[1:])


print remove_x("catxxxdogx")


def remove_x_tr(my_string):
    """
    tail recursive
    """

    def remove_x_acc(my_string_sub, acc):
        if my_string_sub == "":
            return acc
        if my_string_sub[0] != 'x':
            acc = acc + my_string_sub[0]
        return remove_x_acc(my_string_sub[1:], acc)

    return remove_x_acc(my_string, "")


print remove_x_tr("catxxxdogx")

""" 5. Write a function 𝚒𝚗𝚜𝚎𝚛𝚝_𝚡(𝚖𝚢_𝚜𝚝𝚛𝚒𝚗𝚐) that takes the string 𝚖𝚢_𝚜𝚝𝚛𝚒𝚗𝚐 and adds the
character '𝚡' between each pair of consecutive characters in the string. For example, 𝚒𝚗𝚜𝚎𝚛𝚝_𝚡(
"𝚌𝚊𝚝𝚍𝚘𝚐") should return "𝚌𝚡𝚊𝚡𝚝𝚡𝚍𝚡𝚘𝚡𝚐". """


def insert_x(my_string):
    """
    recursive
    """
    if len(my_string) == 1:
        return my_string
    first_char = my_string[0]
    return first_char + 'x' + insert_x(my_string[1:])


print insert_x("catanddogs")


def insert_x_tr(my_string):
    """
    tail recursive
    """

    def insert_x_acc(my_sub_string, acc):
        if len(my_sub_string) == 1:
            acc += my_sub_string
            return acc
        else:
            first_char = my_sub_string[0]
            acc += first_char + 'x'
            return insert_x_acc(my_sub_string[1:], acc)

    return insert_x_acc(my_string, "")


print insert_x_tr("catanddogs")

""" 6. Write a function 𝚕𝚒𝚜𝚝_𝚛𝚎𝚟𝚎𝚛𝚜𝚎(𝚖𝚢_𝚕𝚒𝚜𝚝) that takes a list and returns a new list whose elements
appear in reversed order. For example, 𝚕𝚒𝚜𝚝_𝚛𝚎𝚟𝚎𝚛𝚜𝚎([𝟸, 𝟹, 𝟷]) should return [𝟷, 𝟹, 𝟸]. Do not use
the 𝚛𝚎𝚟𝚎𝚛𝚜𝚎() method for lists. Solution """


def list_reverse(my_list):
    """
    recursive
    """
    if not my_list:
        return []
    return [my_list[-1]] + list_reverse(my_list[:-1])


print(list_reverse([3, 2, 1, -1, -2]))


def list_reverse_tr(my_list):
    """
    tail recursive
    """

    def list_reverse_acc(my_list_sub, acc):
        if not my_list_sub:
            return acc
        acc.append(my_list_sub[-1])
        return list_reverse_acc(my_list_sub[:-1], acc)

    return list_reverse_acc(my_list, [])


print list_reverse_tr([3, 2, 1, -1, -2])


""" 7. Challenge: Write a function 𝚐𝚌𝚍(𝚗𝚞𝚖𝟷, 𝚗𝚞𝚖𝟸) that takes two non-negative integers and computes the
greatest common divisor of 𝚗𝚞𝚖𝟷 and 𝚗𝚞𝚖𝟸. To simplify the problem, you may assume that the greatest common
divisor of zero and any non-negative integer is the integer itself. For an extra challenge, your programs should only
use subtraction. Hint: If you get stuck, try searching for "Euclid's Algorithm". """


def gcd(num1, num2):
    print num1, num2
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

print gcd(15, 12)
print gcd(1071, 462)
print gcd(462, 1071)

"""8. Write a function 𝚜𝚕𝚒𝚌𝚎(𝚖𝚢_𝚕𝚒𝚜𝚝, 𝚏𝚒𝚛𝚜𝚝, 𝚕𝚊𝚜𝚝) that takes as input a list 𝚖𝚢_𝚕𝚒𝚜𝚝 and
two non-negative integer indices 𝚏𝚒𝚛𝚜𝚝 and 𝚕𝚊𝚜𝚝 satisfying 0≤first≤last≤n where n is the length of
𝚖𝚢_𝚕𝚒𝚜𝚝. 𝚜𝚕𝚒𝚌𝚎 should return the corresponding Python list slice 𝚖𝚢_𝚕𝚒𝚜𝚝[𝚏𝚒𝚛𝚜𝚝:𝚕𝚊𝚜𝚝]. For
example, 𝚜𝚕𝚒𝚌𝚎(['𝚊', '𝚋', '𝚌', '𝚍', '𝚎'], 𝟸, 𝟺) should return ['𝚌', '𝚍'].Important: Your solution
should not use Python's built-in slice operator : anywhere in its implementation. Instead use the method 𝚙𝚘𝚙 to
remove one element from the input list during each recursive call. (You may mutate the input list to simplify your
solution.) """


def rec_slice(my_list, start, end):
    if start == 0 and end == 0:
        return []
    first = my_list.pop(0)
    if start > 0:
        return rec_slice(my_list, start - 1, end - 1)
    elif end > 0:
        return [first] + rec_slice(my_list, start, end - 1)

print(rec_slice(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 2, 6))

