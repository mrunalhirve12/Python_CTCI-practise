"""
# O(n) complexity
# Returns split point. If not possible, then
# return -1.
def findSplitPoint(arr, n):
    leftSum = 0
    for i in range(0, n):
        leftSum += arr[i]
        rightSum = 0
        for j in range(i + 1, n):
            rightSum += arr[j]
        if leftSum == rightSum:
            return i + 1
    return -1

def printTwoParts(arr, n):
    splitPo = findSplitPoint(arr, n)

    if splitPo == -1 or splitPo == n:
        print("Not Possible")
        return

    for i in range(0, n):
        if splitPo == i:
            print("")
        print(str(arr[i]) + ' ', end='')
"""


def findSplitPoint(arr, n):
    leftSum = 0
    for i in range(0, n):
        leftSum += arr[i]
    rightSum = 0
    for i in range(n - 1, -1, -1):
        rightSum += arr[i]
        leftSum -= arr[i]
        if rightSum == leftSum:
            return i
    return -1


def printTwoParts(arr, n):
    splitPoint = findSplitPoint(arr, n)

    if splitPoint == -1 or splitPoint == n:
        print("Not Possible")
        return

    for i in range(0, n):
        if splitPoint == i:
            print("")
        print(arr[i], end=" ")

# Driver Code
arr = [1, 2, 3, 4, 5, 5]
n = len(arr)
printTwoParts(arr, n)
