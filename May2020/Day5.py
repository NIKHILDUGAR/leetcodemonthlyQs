#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        gg=[char for char in s] 
        seen = set()
        seen_add = seen.add
        qq= [x for x in gg if not (x in seen or seen_add(x))]
        for i in qq:
            if gg.count(i)==1:
                return gg.index(i)
        return -1
            
