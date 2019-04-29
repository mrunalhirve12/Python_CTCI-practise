# https://leetcode.com/problems/merge-intervals/discuss/180716/Python-solution
"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Idea is to keep track of start and end;
        # if next start is less than end merge intervals
        if not  intervals:
            return []
        intervals = sorted(intervals, key = lambda x: x[0])
        res = []
        start = intervals[0][0]
        end = intervals[0][-1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                res.append([start,end])
                start = intervals[i][0]
                end = intervals[i][-1]
            else:
                end = max(end, intervals[i][-1])
        res.append([start, end])
        return res


s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))