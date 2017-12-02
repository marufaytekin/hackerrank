# coding=utf-8
""" 1. Write a function 𝚝𝚛𝚒𝚊𝚗𝚐𝚞𝚕𝚊𝚛_𝚜𝚞𝚖(𝚗𝚞𝚖) that computes the arithmetic sum 0+1+2...+(num−1)+num. For
example, 𝚝𝚛𝚒𝚊𝚗𝚐𝚞𝚕𝚊𝚛_𝚜𝚞𝚖(𝟹) should return 𝟼. Note that this sum can be computed directly via a simple
arithmetic formula, but use a recursive approach instead. """


def triangular_sum(num):
    if num == 0:
        return 0
    return num + triangular_sum(num - 1)


print(triangular_sum(3))

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


def number_of_threes2(num):
    """
    Tail recursive
    """

    def number_of_threes_sub(num_sub, acc):
        if num_sub == 0:
            return acc
        if num_sub % 10 == 3:
            acc += 1
        return number_of_threes_sub(num_sub / 10, acc)

    return number_of_threes_sub(num, 0)


print(number_of_threes2(34534))

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


def remove_x2(my_string):
    """
    tail recursive
    """

    def remove_x_sub(my_string_sub, acc):
        if my_string_sub == "":
            return acc
        if my_string_sub[0] != 'x':
            acc = acc + my_string_sub[0]
        return remove_x_sub(my_string_sub[1:], acc)

    return remove_x_sub(my_string, "")


print remove_x2("catxxxdogx")

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


def insert_x2(my_string):
    """
    tail recursive
    """
    def insert_x_sub(my_string_sub, acc):
        if len(my_string_sub) == 1:
            acc += my_string_sub
            return acc
        else:
            first_char = my_string_sub[0]
            acc += first_char + 'x'
            return insert_x_sub(my_string_sub[1:], acc)

    return insert_x_sub(my_string, "")


print insert_x2("catanddogs")