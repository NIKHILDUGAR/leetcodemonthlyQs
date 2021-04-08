class Solution(object):
    def halvesAreAlike(self, s):
        su1=0
        su2=0
        s=s.lower()
        a="aeiou"
        for i in a:
            su1=su1+s[:int(len(s)/2)].count(i)
            su2=su2+s[int(len(s)/2):].count(i)
        return(su1==su2)
