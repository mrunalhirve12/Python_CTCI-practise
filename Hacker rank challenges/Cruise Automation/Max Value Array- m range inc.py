"""
Consider an array of size n with all initial values as 0, we need to perform following m range increment operations.

increment(a, b, k) : Increment values from 'a'
                     to 'b' by 'k'.
After m operations, we need to calculate the maximum of the values in the array.

Examples:

Input : n = 5 m = 3
        a = 0, b = 1, k = 100
        a = 1, b = 4, k = 100
        a = 2, b = 3, k = 100
Output : 200
Explanation:
Initially array = {0, 0, 0, 0, 0}
After first operation:
array = {100, 100, 0, 0, 0}
After second operation:
array = {100, 200, 100, 100, 100}
After third operation:
array = {100, 200, 200, 200, 100}
Maximum element after m operations
is 200.

Input : n = 4 m = 3
        a = 1, b = 2, k = 603
        a = 0, b = 0, k = 286
        a = 3, b = 3, k = 882
Output : 882
Explanation:
Initially array = {0, 0, 0, 0}
After first operation:
array = {0, 603, 603, 0}
After second operation:
array = {286, 603, 603, 0}
After third operation:
array = {286, 603, 603, 882}
Maximum element after m operations
is 882.
"""
import sys
"""
# A naive method is to perform each operation on given range and then at last find the maximum number
# Time Complexity: O(m * max(range)). Here max(range) means maximum elements to which k is added in a single operation.


def maxArray(arr, a, b, k):
    for i in range(len(a)):
        lowerBound = a[i]
        upperBound = b[i]
        max = - sys.maxsize - 1
        for j in range(lowerBound, upperBound + 1):
            arr[j] += k[i]
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max
"""


def maxArray(arr, a, b, k):
    max = - sys.maxsize - 1
    for i in range(len(a)):
        lowerBound = a[i]
        upperBound = b[i]
        if lowerBound == upperBound:
            arr[upperBound] += k[i]
        else:
            arr[lowerBound] += k[i]
            arr[upperBound] += k[i]
    for i in range(len(arr)):
        sums = arr[i]
        if max < sums:
            max = sums
    return max


print(maxArray([0, 0, 0, 0], [1, 0, 3], [2, 0, 3], [603, 286, 882]))

