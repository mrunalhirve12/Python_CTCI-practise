"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    if len(nums) < 1:
        return False
    else:
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[target - nums[i]] = i
            else:
                return [dict[nums[i]], i]

twoSum([2,3,4,7, 6, 11,15], 9)

"""
Assuming we have to return the first pair of numbers instead of its index position
"""
def sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    arr = []
    if len(nums) < 1:
        return False
    else:
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp not in arr:
                arr.append(nums[i])
            else:
                return (temp, nums[i])

sum([2,3,4,7, 6, 11,15], 9)

"""
Assuming we want O(1) space complexity and want return the first pair of numbers instead of its index position
"""
def sumlessspace(nums, target):
    nums.sort
    l = 0
    r = len(nums) - 1
    while l < r :
        if nums[l] + nums[r] == target:
            a = [l, r]                  # if we have to return index, then this code wont work as we are using sorting
            b =[nums[l], nums[r]]       # if numbers are to be returned then we can consider
            return [nums[l], nums[r]]
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1
    return 0

sumlessspace([3,2,4], 6)