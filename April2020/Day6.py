# question link https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3288/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list) 
        for ele in strs: 
            temp[str(sorted(ele))].append(ele) 
        res = list(temp.values())
        res.sort()
        return res
