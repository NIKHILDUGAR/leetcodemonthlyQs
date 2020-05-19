# Question link- https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3291/
# repeted iteration and updation method
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S1 = [char for char in S]
        T1 = [char for char in T]
        s1=[]
        t1=[]
        for i in range(0, len(S)):  
            if S[i] != '#':  
                s1.append(S[i])  
            elif len(s1) != 0:  
                s1.pop()     
        for i in range(0, len(T)):  
            if T[i] != '#':  
                t1.append(T[i])  
            elif len(t1) != 0:  
                t1.pop() 
        if len(s1)==len(t1):
            for i in range(len(s1)):
                if s1[i]!=t1[i]:
                    return False
        else:
            return False
        return True
#TWO POINTER METHOD 
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
