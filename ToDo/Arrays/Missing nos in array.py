#Leetcode 268
# bit manipulation
from pip._vendor.msgpack.fallback import xrange


def missingNumber1(self, nums):
    res = 0
    for i in xrange(len(nums)+1):
        res ^= i
    for num in nums:
        res ^= num
    return res