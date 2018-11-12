# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.dfs(root,0,sum,[])
        return self.ans
    
    def dfs(self,root,sumNow,sum,path):
        if not root :
            return
        elif not root.left  and not root.right :
            if root.val + sumNow == sum:
                self.ans.append(path+[root.val])
                return
            else:
                return
        else:
            if root.left:
                self.dfs(root.left,sumNow+root.val,sum,path+[root.val])
            if root.right:
                self.dfs(root.right,sumNow+root.val,sum,path+[root.val])
