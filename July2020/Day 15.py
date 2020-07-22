class Solution:
    def reverseWords(self, s: str) -> str:
        s=" ".join(s.split())
        c=""
        for i in s.split()[::-1]:
            c+=i+" "
        return(c.strip())