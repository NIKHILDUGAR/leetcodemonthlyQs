# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        gg=[int for int in nums] 
        seen = set()
        seen_add = seen.add
        qq= [x for x in gg if not (x in seen or seen_add(x))]
        for i in qq:
            if gg.count(i)==1:
                return (i)
        return -1
