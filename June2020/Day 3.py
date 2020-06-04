
#easy to understand solution
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs=sorted(costs,key=lambda x:x[0]-x[1])
        c=0
        # print(costs[0:len(costs)//2][0])
        for i in range(len(costs)//2):
            c+=costs[i][0]
        for i in range(len(costs)//2,len(costs)):
            c+=costs[i][1]
        return c
#One-liner 
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum([i for i, j in costs]) + sum(sorted([j - i for i,j in costs])[:len(costs)//2])
