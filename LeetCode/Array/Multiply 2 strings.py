class Solution(object):
    def multiply(self, num1, num2):
        """
        #:type num1: str
        #:type num2: str
        #:rtype: str

        # Using ord function
        res1 = res2 = 0
        # ord gives the unicode value
        for i in num1:
            res1 = 10 * res1 + (ord(i) - ord('0'))
        for i in num2:
            res2 = 10 * res2 + (ord(i) - ord('0'))
        return str(res1 * res2)
        """

        # simple calculation
        result = 0
        for i, digit1 in enumerate(num1[::-1]):
            temp1 = int(digit1) * (10**i)
            for j, digit2 in enumerate(num2[::-1]):
                temp2 = int(digit2) * (10 ** j)
                result += temp1 * temp2

        return str(result)


s = Solution()
print(s.multiply("123", "456"))
