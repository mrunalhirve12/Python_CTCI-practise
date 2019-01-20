#can a string form palindrome
from collections import Counter


def permuatation (str1):
    counter = Counter()  # dict subclass for counting hashable objects
    for c in str1:
        counter[c] += 1
    odd = 0
    for c in counter:
        if counter[c] & 1:
            odd += 1
        if odd > 1:
            return False
    return True

if permuatation('aabbcdd'):
    print("Permuation of Palindrome")
else:
    print("Not Permuation of Palindrome")
