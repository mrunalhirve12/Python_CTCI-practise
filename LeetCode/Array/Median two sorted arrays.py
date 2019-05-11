"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # idea to traverse just first half ot the 2 array
        # keep updated a array according (2 values)
        # depending on len of total elents in 2 array; return the median
        m = len(nums1)
        n = len(nums2)
        mn = m + n
        nums1.append(10 ** 10)  # prevent index out-of-range
        nums2.append(10 ** 10)
        i = 0
        j = 0
        a = [0] * 2
        while i + j <= mn / 2:
            if nums1[i] < nums2[j]:
                a[(i + j) % 2] = nums1[i]  # save latest number (alternating 0 or 1)
                i += 1
            else:
                a[(i + j) % 2] = nums2[j]
                j += 1
        if mn % 2:  # odd length
            return a[int(mn / 2 % 2)]
        else:  # even length
            return sum(a) / 2.0

s = Solution()
print(s.findMedianSortedArrays([1, 3, 5], [2, 4]))
