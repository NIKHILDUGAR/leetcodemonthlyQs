class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = [1]*(rowIndex + 1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                l[j] += l[j-1]
        return l
