import collections

from pip._vendor.msgpack.fallback import xrange

NO_CHARS = 256


# 2 for loop solution does not work
# ------------------- O(n logn n solution)---------------------------------------------------------------
def isPermutation(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    if len_str1 != len_str2:
        print("No")

    str1 = sorted(str1)  # returns sorted array of the string
    str2 = sorted(str2)

    for i in range(len_str1):
        if str1[i] != str2[i]:
            print("No")
            break
        print("yes")


isPermutation('hgjgjg', 'jfjfjf')


# ---Time Complexity : O(n), Space Complexity : O(n)-------------------------------------------------------------------------
def arePermutation(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    if len_str1 != len_str2:
        return 0

    count1 = [0] * NO_CHARS
    count2 = [0] * NO_CHARS

    for i in str1:
        count1[ord(i)] += 1  # return an integer representing the Unicode code point of the character

    for i in str2:
        count2[ord(i)] += 1

    for i in xrange(NO_CHARS):
        if count1[i] != count2[i]:
            return 0
    return 1


if arePermutation('hgjgjg', 'jfjfjf'):
    print("yes")
else:
    print("no")


# -------------------------------------------------------------------
def are_permutations(str1, str2):
    """Returns True if the first given string is a permutation of the second

    given string.
    """
    perm = collections.defaultdict(int)
    for char in str1:
        perm[char] += 1
    for char in str2:
        perm[char] -= 1

    return not any(perm.values())


if are_permutations('abc', 'dca'):
    print("yes")
else:
    print("no")


l = "   mru    "
m= l.lstrip().rstrip()
print(l)