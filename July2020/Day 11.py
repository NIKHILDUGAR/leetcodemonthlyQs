# CORRECT AND FASTER SOLUTION BUT WRONG ORDER
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sublist = [[]] 
        for i in range(len(nums) + 1):   
            for j in range(i + 1, len(nums) + 1): 
                sub = nums[i:j] 
                sublist.append(sub) 
        return sublist
        
#CORRECT AND SLOWER SOLUTION
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
