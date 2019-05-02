"""
Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’.
"""

"""
# NAIVE SOLUTION
# Time Complexity : O(n2)
# Auxiliary Space : O(1)
def getPairsCount(arr, n, sum):
    count = 0  # Initialize result
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1

    return count
"""


def getPairsCount(arr, n, sum):
    dict = {}
    res = []
    for i in range(n):
        target = sum - arr[i]
        if arr[i] not in dict:
            dict[target] = i
        else:
            res.append((arr[i], target))
    return res


# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print(getPairsCount(arr, n, sum))
