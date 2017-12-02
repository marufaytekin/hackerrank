def is_palindrome(word):
    if len(word) < 2:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])


print is_palindrome("abcba")
print is_palindrome("abcdeedcba")
print is_palindrome("abcdeedcbaz")
