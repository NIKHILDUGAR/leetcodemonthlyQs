#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = set()
        seen_add = seen.add
        qq= [x for x in nums if not (x in seen or seen_add(x))]
        for i in qq:
            if nums.count(i)>len(nums)//2:
                return i
