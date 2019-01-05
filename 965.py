# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.search(root,root.val)
    def search(self,node,value):
        if node.val != value:
            return False
        if node.left != None and node.right != None:
            lr = self.search(node.left,value)
            rr = self.search(node.right,value)
            return lr and rr
        if node.left != None and node.right == None:
            return self.search(node.left,value)
        if node.left == None and node.right != None:
            return self.search(node.right,value)
        else: return True
        
        
        
class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node):
            return not node or node.val==root.val and dfs(node.left) and dfs(node.right)
        return dfs(root)
