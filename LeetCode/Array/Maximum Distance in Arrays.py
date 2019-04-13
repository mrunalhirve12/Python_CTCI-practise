"""
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
"""
import sys


class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        """
        # Fails for test case 2, as we want to select just 1 element from one array
        
        max = -sys.maxsize - 1
        for i in range(len(arrays)):
            for j in range(len(arrays)):
                n = len(arrays[j])
                maxdiff = arrays[j][n - 1] - arrays[i][0]
                if maxdiff > max:
                    max = maxdiff
        return max
        """

        """
        # It just checks iteratively and not previous elements so gives output as 12 but expected 14
        # Complexity (n)
        # initializing my res with 0, maxx is the last index of first array and min is 0th index of first array
        res = 0
        maxx = arrays[0][-1]
        minn = arrays[0][0]
        # iterate through all the arrays
        for i in range(1, len(arrays)):
            # the max diff can be cross (i.e last element of last element of first array & first element of ith array
            # OR
            # last element of ith array with min element from previous array)
            newres = max(abs(arrays[i][0] - maxx), abs(arrays[i][-1] - minn))
            # update the max
            res = max(newres, res)
            # update the min and max to store current arrays 0th and nth location
            maxx = arrays[i][-1]
            minn = arrays[i][0]
        return res
        """

        # Possible fix with attempt 2 can be always maintain the min and max element so far
        # initializing my res with 0, maxx is the last index of first array and min is 0th index of first array
        res = 0
        maxx = arrays[0][-1]
        minn = arrays[0][0]
        # iterate through all the arrays
        for i in range(1, len(arrays)):
            # the max diff can be cross (i.e last element of last element of first array & first element of ith array
            # OR
            # last element of ith array with min element from previous array)
            newres = max(abs(arrays[i][0] - maxx), abs(arrays[i][-1] - minn))
            # update the max
            res = max(newres, res)
            # update the min and max to store current min and max found so far
            maxx = max(maxx, arrays[i][-1])
            minn = min(minn,arrays[i][0])
        return res


s = Solution()
print(s.maxDistance([[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]))

"""
TestCase #1
print(s.maxDistance([[1,2,3],[4,5],[1,2,3]]))

TestCase #2
print(s.maxDistance([[1,4],[0,5]]))

TestCase #3
print(s.maxDistance([[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]))
"""