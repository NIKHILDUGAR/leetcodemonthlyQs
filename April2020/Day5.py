class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inff=-1000000
        bs=inff
        bws=0
        for i in prices:
            bs=max(bs,bws-i)
            bws=max(bws,bs+i)
        return bws
