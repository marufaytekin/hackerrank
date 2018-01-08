

def is_substring(s1, s2, m, n):
    if m == 0:
        return True
    if n == 0:
        return False
    if s1[m-1] == s2[n-1]:
        return is_substring(s1, s2, m-1, n-1)
    return is_substring(s1, s2, m, n-1)

a = "def"
b = "abcdefg"
print is_substring(a, b, len(a), len(b))