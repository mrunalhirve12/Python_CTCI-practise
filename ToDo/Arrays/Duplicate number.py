# Leetcode: 287
# https://leetcode.com/problems/find-the-duplicate-number/discuss/73101/Python-two-pointer-solution.
def findDuplicate( nums):
    slow = fast = head = len(nums)
    slow = nums[slow-1]
    fast = nums[nums[fast-1]-1]
    while slow != fast:
        slow = nums[slow-1]
        fast = nums[nums[fast-1]-1]
    while head != slow:
        head = nums[head-1]
        slow = nums[slow-1]
    return head

findDuplicate([1,3,4,2,2])