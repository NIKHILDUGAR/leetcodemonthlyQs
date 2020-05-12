# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/  
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c=0
        for i in S:
            if i in J:
                c+=1
        return c
