# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root,0,sum)
        
        
    def dfs(self,start,sumNow,sum):
        if start == None:
            return False
        elif start.left == None and start.right == None:
            if sumNow + start.val == sum:
                return True
            else :
                return False
        else:
            return (self.dfs(start.left,sumNow+start.val,sum))or(self.dfs(start.right,sumNow+start.val,sum))
            
        
        
