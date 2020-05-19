# question link - https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3308/
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i=0
        while(m!=n):
            m>>=1
            n>>=1
            i+=1
        return n<<i
