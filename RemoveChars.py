def string_reduce(input_string):
    """
    Given a string of characters change all occurrences of
    two or more consecutive 'e's with a single 'e'.
    Example:
    Input: 'asdheeeeskaeeeleee'
    Output: 'asdheskaele'
    Args: input_string String
    """
    o = []
    in_list = list(input_string)
    first = ''
    for c in in_list:
        if c is not first:
            o.append(c)
            first = c

    return ''.join(o)


print(string_reduce("aaddaafffffergggg"))