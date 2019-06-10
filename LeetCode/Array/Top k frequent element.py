"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter
import heapq

# Complexity is O(Nlog(K)) O(N)

class Solution(object):
    def topKFrequent(self, nums, k):
        d, h = [(freq, num) for num, freq in Counter(nums).items()], []
        for i in range(k):
            heapq.heappush(h, d[i])
        for i in range(k, len(d)):
            if d[i][0] > h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h, d[i])
        return [heapq.heappop(h)[1] for _ in range(k)][::-1]