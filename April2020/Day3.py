# question link- https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -10000000000
        max_ending_here = 0
        for i in range(len(nums)): 
            max_ending_here = max_ending_here + nums[i] 
            if (max_so_far < max_ending_here): 
                max_so_far = max_ending_here 
            if max_ending_here < 0: 
                max_ending_here = 0   
        return max_so_far 
