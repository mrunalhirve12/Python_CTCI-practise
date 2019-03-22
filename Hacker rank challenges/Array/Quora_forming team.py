class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()

        return self.combSum2(candidates, target)

    def combSum2(self, candidates, target):

        ans = []
        old = -1
        for i, x in enumerate(candidates):
            if x == old:
                continue
            if x > target:
                return ans
            if x == target:
                return ans + [[x]]

            t = self.combSum2(candidates[i + 1:], target - x)

            for a in t:
                ans += [[x] + a]

            old = x

        return ans

    obj = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(obj.combinationSum2(candidates, target))

s = Solution()
s.combinationSum2([10,1,2,7,6,1,5], 8)