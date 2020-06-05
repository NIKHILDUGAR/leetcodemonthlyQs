#Question link- https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3351/

import numpy as np
class Solution:
    
    def __init__(self, w: List[int]):
        self.sum=sum(w)
        self.wsum=np.cumsum(w)
        
    def pickIndex(self) -> int:
        index=random.randint(1,self.sum)
        return self.bs(index)
    def bs(self,val): # binary search
        l=0
        r=len(self.wsum)-1
        while l<r:
            m=int(l+(r-l)/2)
            if self.wsum[m]<val:
                l=m+1
            else:
                r=m
        return l
