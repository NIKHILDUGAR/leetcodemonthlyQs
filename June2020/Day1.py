class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if (root == None): 
            return root
        right=root.right          
        root.right=self.invertTree(root.left)  
        root.left=self.invertTree(right)  
        return root
