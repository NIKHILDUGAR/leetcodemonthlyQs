question link - https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/
# naive approach
class Solution:
    def isHappy(self, n: int) -> bool:
        if (n == 1 or n == 7) :
            return True
        sum = n
        x = n
        while(sum > 9):
            sum = 0
            while (x > 0):
                d= x%10
                sum += d*d
                x//=10
            if (sum == 1) :
                return True
            x = sum
        if(sum == 7):
            return True 
        return False        
