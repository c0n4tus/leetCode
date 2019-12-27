# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.maxDepth(root) != None
    
    
    def maxDepth(self,root:TreeNode) -> int:
        if root == None:
            return 0
        
        leftDepth=self.maxDepth(root.left)
        rightDepth=self.maxDepth(root.right)
        
        if leftDepth == None or rightDepth == None:
            return None
        
        if abs(leftDepth - rightDepth) > 1:
            return None
        
        return max(leftDepth,rightDepth) + 1
            
    
        