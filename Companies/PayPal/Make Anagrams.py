import collections


def solution(A, B):
    # write your code in Python 3.6
    """a = collections.Counter(A)
    b = collections.Counter(B)
    counter = 0
    for i in a:
        if i in b:
            if a[i] != b[i]:
                counter += abs(a[i] - b[i])
        else:
            counter += 1
    return counter"""

    dict1 = {}
    dict2 = {}
    for i in range(len(A)):
        if A[i] not in dict1:
            dict1[A[i]] = 1
        else:
            dict1[A[i]] += 1
    for i in range(len(B)):
        if B[i] not in dict2:
            dict2[B[i]] = 1
        else:
            dict2[B[i]] += 1
    counter = 0
    for letter in dict1:
        if letter in dict2:
            if dict1[letter] != dict2[letter]:
                counter += abs(dict1[letter] - dict2[letter])
                if dict1[letter] > dict2[letter]:
                    dict2[letter] = dict1[letter]
        else:
            dict2[letter] = dict1[letter]
            counter += dict1[letter]
    for letter in dict2:
        if letter in dict1:
            if dict2[letter] != dict1[letter]:
                counter += abs(dict2[letter] - dict1[letter])
                if dict2[letter] > dict1[letter]:
                    dict1[letter] = dict2[letter]
        else:
            dict1[letter] = dict2[letter]
            counter += dict2[letter]
    return counter




print(solution("apple", "pear"))