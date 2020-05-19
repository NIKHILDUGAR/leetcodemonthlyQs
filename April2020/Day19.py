# question link-https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3304/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try :
            return nums.index(target)
        except:
            return -1
