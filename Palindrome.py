def is_palindrome(s):
    l = list(s)
    size = len(l)
    for i in range(int(size / 2)):
        if l[i] is not l[-(i + 1)]:
            return False
    return True



def ris_palindrome(s):
    """
    Recursive Palindrome
    """
    size = len(s)
    if size == 0 or size == 1:
        return True
    if s[0] is not s[size - 1]:
        return False
    return ris_palindrome(s[1:-1])


s1 = 'I am not a palindrome'
s2 = 'zxaabcbaaxz'

print(is_palindrome(s1))
print(is_palindrome(s2))

print(ris_palindrome(s1))
print(ris_palindrome(s2))
