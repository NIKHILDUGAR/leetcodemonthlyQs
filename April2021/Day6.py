class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        return(int(sum(abs(n-(2*i+1)) for i in range(n))/2))
