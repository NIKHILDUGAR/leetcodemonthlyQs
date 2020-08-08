class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=[]
        s=set()
        for i in (nums):
            if i in s:
                l.append(i)
            s.add(i)
        return l
