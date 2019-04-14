"""
Find max difference between elements in an array


Maximum difference between two elements such that larger element appears after the smaller number
Given an array arr[] of integers, find out the maximum difference between any two elements such that
larger element appears after the smaller number.

https://www.geeksforgeeks.org/maximum-difference-between-two-elements/
"""

"""
NAIVE APPROACH O(n2)
In the outer loop, pick elements one by one and 
in the inner loop calculate the difference of the picked element with every other element in the array and 
compare the difference with the maximum difference calculated so far. 

def maxdiff(arr):
    max_diff = arr[1] - arr[0]
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] - arr[i] > max_diff:
                max_diff = arr[j]- arr[i]
    return max_diff
"""
# ==============================================================================================================

"""
OPTIMIZED APPROACH 1: TIME COMPLEXITY :O(n) & SPACE COMPLEXITY: O(1)
Take difference of the picked element with every other element, 
we take the difference with the minimum element found so far. So we need to keep track of 2 things:
1) Maximum difference found so far (max_diff).
2) Minimum number visited so far (min_element).



def maxdiff(arr):
    min_elem = arr[0]
    max_diff = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if arr[i] - min_elem > max_diff:
            max_diff = arr[i] - min_elem
        if arr[i] < min_elem:
            min_elem = arr[i]
    return max_diff


print(maxdiff([2, 3, 10, 6, 4, 8, 1]))
"""

#==========================================================================================================


#OPTIMIZED APPROACH 2: TIME COMPLEXITY :O(n) & SPACE COMPLEXITY: O(1)
#We can also keep track of max element from right side


def maxdiff(arr):
    max_diff = -1
    n = len(arr)
    max_elem = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] > max_elem:
            max_elem = arr[i]
        else:
            if max_elem - arr[i] > max_diff:
                max_diff = max_elem - arr[i]
    return max_diff

print(maxdiff([2, 3, 10, 6, 4, 8, 1]))


#=======================================================================================================

