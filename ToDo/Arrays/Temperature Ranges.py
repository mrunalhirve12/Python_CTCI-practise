#https://leetcode.com/problems/daily-temperatures/discuss/109858/Simple-Python-by-hashing-the-temperatures
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # Time: O(n.k), where k is the range of the temperature.
        # Space: O(n + k)
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if not stack:
                stack.append(i)
            else:
                res[i] = stack[-1] - i
                stack.append(i)
        return res

s = Solution()
s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])