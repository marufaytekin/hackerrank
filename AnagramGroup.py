"""
Group Anagram: Read in N Strings and determine if they are anagrams of each other.
Ex:
'cat','act','tac' -> true
'cat', 'bat', 'act' -> false
"""


def anagram(str_list):
    sorted_list = []
    for item in str_list:
        sorted_item = sorted(list(item))
        sorted_list.append(''.join(sorted_item))
    for item in sorted_list:
        if item != sorted_list[0]:
            return False
    return True

l1 = ["cat", "act", "tac"]
l2 = ["cat", "bat", "act"]

print anagram(l1)
print anagram(l2)
