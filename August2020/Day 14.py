class Solution:
    def longestPalindrome(self, s: str) -> int:
        c={}
        for i in s:
            c[i]=c.get(i,0)+1
        r=0
        parit=False
        for i,j in c.items():
            if j%2==0:
                r+=j
            else:
                parit=True
                r+=j-1
        if parit:
            r+=1
        return r
