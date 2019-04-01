"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
import heapq



class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or not k:
            return None
        """
        #MAX HEAP: Time complexity: O(n + k log n). Space complexity: O(n).
        heap = [-n for n in nums]
        heapq.heapify(heap)
        for i in range(k):
            res = heapq.heappop(heap)
        return -res
        

        # MIN HEAP: O(k + (n-k) log k). Space complexity: O(k)
        # make heap size of k
        heap = nums[:k]
        #heapify heap
        heapq.heapify(heap)
        #chk for remaining elements
        for i in range(k, len(nums)):
            #if num > than heap heapelement and
            if nums[i] > heap[0]:
                heapq.heappushpop(heap, nums[i])
        return heapq.heappop(heap)
        """

        def partition(A, p, r):
            idx = random.randint(p, r)
            A[idx], A[r] = A[r], A[idx]
            i = p - 1
            for j in range(p, r):
                if A[j] <= A[r]:
                    i += 1
                    A[i], A[j] = A[j], A[i]
            i += 1
            A[i], A[r] = A[r], A[i]
            return i

        def quickselect(A, p, r, i):
            if p == r:
                return A[p]
            q = partition(A, p, r)
            k = q - p + 1
            if k == i:
                return A[q]
            elif k > i:
                return quickselect(A, p, q - 1, i)
            else:
                return quickselect(A, q + 1, r, i - k)

        return quickselect(nums, 0, len(nums) - 1, len(nums) - k + 1)

s = Solution()
s.findKthLargest([3,2,1,5,6,4],2)