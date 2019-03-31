"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        #similar to two sum
        dict = {}
        #iterate through list
        for i in range(len(numbers)):
            #calculate diff, store diff map index
            diff = target - numbers[i]
            if numbers[i] in dict:
              #return indexes of numbers having sum  
              return [dict[numbers[i]]+1, i+1]
            else:
                dict[diff] = i
        """

        #using two pointers
        left, right = 0, len(numbers) - 1
        sum = 0
        #iterate while left < right
        while left < right:
            #calculate sum of left and right, if sum return else move left is sum less else move right
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1


s = Solution()
print(s.twoSum([0,0,3,4],0))

"""
TestCase #1
s.twoSum([2,7,11,15], 9)

TestCase #2
s.twoSum([2,7,11,15], 9)

TestCase #3
s.twoSum([0,0,3,4],0)
"""