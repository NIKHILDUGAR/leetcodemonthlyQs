#QUESTION LINK - https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/
# NAIVE approach  
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        l={}
        for i in nums:  
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        for k,v in l.items():
            if v==1:
                return k
#BETTER APPROACH - BIT MANIPULATION
class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a
