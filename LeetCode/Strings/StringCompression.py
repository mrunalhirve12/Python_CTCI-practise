class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res = []
        count = 1
        for i in range(len(chars)-1):
            if chars[i] == chars[i+1]:
                count += 1

            else:
                res.append(chars[i])
                if count > 1:
                    count = str(count)
                    count = count.split()
                    res = res + count
                count = 1

        res.append(chars[i])
        if count > 1:
            count = str(count)
            count = count.split()
            res = res + count
        return res

s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))