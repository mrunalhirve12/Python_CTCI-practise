"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # What we want to do over here is just return the change the array make it distinct at start in place
        # we are not concerned what happens to array at the end.
        if not nums:
            return 0
        length = 1
        i = 0
        # Initialize two pointers i = 0, j = 1.
        # Iterate j over range(1, len(nums)), and if nums[j] != nums[i],
        # we increment i by 1, and swap nums[i] and nums[j]
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
                length += 1
        return nums


s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4],))

"""
Test Case #1
s.removeDuplicates([1,1,2])

Test Case #2
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4],)
"""