"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ref_array = []
        self.length = 0

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # keep a sorted array
        # use binary search to find insertion index

        low = 0
        high = self.length - 1

        while low <= high:
            mid = (low + high) // 2
            if self.ref_array[mid] >= num:
                high = mid - 1
            else:
                low = mid + 1

        self.ref_array.insert(low, num)
        self.length += 1

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        # as array is always sorted we can always use the same median property

        if self.length % 2 == 0:
            temp = self.length // 2
            return (self.ref_array[temp] + self.ref_array[temp - 1]) / 2.0
        else:
            return self.ref_array[self.length // 2]