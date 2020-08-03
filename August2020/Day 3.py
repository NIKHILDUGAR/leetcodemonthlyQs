class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[char for char in s]
        stir=""
        for i in range(len(l)):
            if l[i].isupper() or l[i].islower() or l[i].isnumeric():
                stir+=l[i].lower()
        if stir==stir[::-1]:
            return True
