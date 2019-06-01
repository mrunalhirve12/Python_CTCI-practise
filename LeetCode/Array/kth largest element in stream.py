"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""
import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heapque = []

        # O(k*log(k))
        for i in nums[:k]:
            heapq.heappush(self.heapque, i)

        # O( (n-k)logk )
        if nums[k:]:
            for i in nums[k:]:
                if i > self.heapque[0]:
                    heapq.heappop(self.heapque)
                    heapq.heappush(self.heapque, i)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heapque) < self.k:
            # O( log(k) )
            heapq.heappush(self.heapque, val)
        elif val > self.heapque[0]:
            # O( log(k) )
            heapq.heappop(self.heapque)
            heapq.heappush(self.heapque, val)

        if len(self.heapque) < self.k:
            return -1
        return self.heapque[0]

# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [4,5,8,2]
obj = KthLargest(3, nums)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))

