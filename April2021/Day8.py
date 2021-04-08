# Question link- https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3701/
class Solution(object):
    def letterCombinations(self, digits):
        l = []
        d = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        if len(digits) == 0:
            return l
        l=[i for i in d[int(digits[0])]]
        for i in digits[1:]:
            l = [str(j) + str(io) for j in l for io in d[int(i)]]
        return l