class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        while True:
            n=n-i
            if n<0:
                break
            i=i+1
        return i-1
