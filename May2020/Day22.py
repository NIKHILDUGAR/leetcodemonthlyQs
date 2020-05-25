# question link - https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3337/
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        l=list(s)
        result = [item for items, c in Counter(l).most_common() for item in [items] * c] 
        
        r="".join(result)
        return r
