"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x: x.start)
        heap = []
        heapq.heapify(heap)
        res = 1
        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval.end)
            else:
                if heap[0] <= interval.start:
                    heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
            res = max(res, len(heap))
        return res
