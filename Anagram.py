def is_anagram(a, b):
    if len(a) != len(b):
        return False
    a_list = list(a)
    b_list = list(b)
    a_list.sort()
    b_list.sort()
    a_str = ''.join(a_list)
    b_str = ''.join(b_list)
    print(a_str)
    print(b_str)
    return a_str == b_str


def number_needed(a, b):
    a_list = list(a)
    b_list = list(b)
    arr = [0] * 26
    for c in a_list:
        arr[ord(c) - ord('a')] += 1
    for c in b_list:
        arr[ord(c) - ord('a')] -= 1
    cnt = 0;
    for i in arr:
        cnt += abs(i)
    return cnt


def number_needed2(a, b):
    a_list = list(a)
    b_list = list(b)
    dic = {}
    for c in a_list:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    for c in b_list:
        if c in dic:
            dic[c] -= 1
        else:
            dic[c] = -1
    cnt = 0;
    for k in dic:
        cnt += abs(dic[k])
    return cnt


a = "adcb"
b = "cbde"

print(is_anagram(a, b))

print(number_needed(a, b))

print number_needed2(a, b)