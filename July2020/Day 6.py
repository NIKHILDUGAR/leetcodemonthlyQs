class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int(''.join(map(str, digits)))
        s+=1
        res = [int(x) for x in str(s)]
        return res
        