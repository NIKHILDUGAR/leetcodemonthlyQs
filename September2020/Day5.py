# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l=[]
        def printInorder(self): 
            if self: 
                printInorder(self.left) 
                l.append(self.val)
                printInorder(self.right) 
        printInorder(root1)
        printInorder(root2)
        return sorted(l)
