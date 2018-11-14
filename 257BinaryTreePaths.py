# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        arrow = '->'
        result = []
        
        def dfs(root,s):
            if not root.left and not root.right:
                result.append(s+str(root.val))
            else:
                if root.left:
                    dfs(root.left, s+str(root.val)+arrow)
                if root.right:
                    dfs(root.right, s+str(root.val)+arrow)
        if not root:
            return []
        dfs(root,'')
        return result
