#question link - https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3286/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=[0]*nums.count(0)
        for i in range(nums.count(0)):
                nums.remove(0)
        for i in l:
            nums.append(i)
        
