"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
"""
from pip._vendor.msgpack.fallback import xrange


#Bit Manipulation

class Solution(object):
    def grayCode(self, n):

        #:type n: int
        #:rtype: List[int]
        
        res = []
        # 1 << n ; multiply by 2 i.e n = 2 ; 1<<n = 4
        for i in range(1<<n):
            #doing xor with previous no. i.e 0>>1=0; 1>>1 = 0; 2>>1=1 and so on,
            # to get gray code we need to XOR previous no with present no
            res.append(i^(i>>1))
        return res

s = Solution()
print(s.grayCode(2))
