"""
Given a string of characters
change all occurrences of two or more consecutive 'e's with a single 'e'.

Example:
Input: 'asdheeeeskaeeeleee'
Output: 'asdheskaele'
Args: input_string String
"""


def string_reduce(input_string):
    o = []
    in_list = list(input_string)
    curr = ''
    for c in in_list:
        if c is not curr:
            o.append(c)
            curr = c

    return ''.join(o)


print(string_reduce("aaddaaffffferggggzzzzz"))