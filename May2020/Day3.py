#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga=[char for char in magazine] 
        for i in ransomNote:
            try:
                maga.remove(i)
            except:
                return False
        return True
