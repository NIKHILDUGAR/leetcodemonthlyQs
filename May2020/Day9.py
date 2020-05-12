#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num**0.5==int(num**0.5):
            return True
