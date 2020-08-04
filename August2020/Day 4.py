# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3412/
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num>0:
            return (math.ceil(math.log10(num) /math.log10(4)) == math.floor(math.log10(num) /math.log10(4)))
        else:
            return False
        
