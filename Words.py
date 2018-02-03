"""
find all possible words from given characters
"""

import itertools


def all_words(letters):
    for word in itertools.permutations(letters):
        print word, ''.join(word)


all_words("cat")
