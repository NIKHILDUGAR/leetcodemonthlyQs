# Question link- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3657/
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return int(min(len(list(set(candyType))),len(candyType)/2))