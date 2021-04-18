class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ss = set(s)
        
        while True:
            temp = s
            for val in ss:
                if val*k in s:
                    s = s.replace(val*k, '')
            if temp == s:
                return s
