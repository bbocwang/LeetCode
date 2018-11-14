# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if (self.height(root.left) - self.height(root.right)) not in [1,0,-1]:
            return False
        else:
            if root.left == None and root.right == None:
                return True
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def height(self,root):
        if not root:
            return 0
        else:
            return max(self.height(root.left),self.height(root.right)) + 1
        
        

second approch:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1
            
        if not root:
            return True
        else:
            return check(root) != -1
        
