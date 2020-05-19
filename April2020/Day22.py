#question- https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3307/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict 
        prevSum = defaultdict(lambda : 0) 
        res = 0 
        currsum = 0 
        for i in range(0, len(nums)):   
            currsum += nums[i]  
            if currsum == k:   
                res += 1         
            if (currsum - k) in prevSum: 
                res += prevSum[currsum - k]  
            prevSum[currsum] += 1
        return(res)
