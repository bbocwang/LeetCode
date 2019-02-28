# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        maxLevel = 0
        def dfs(node,level):
            if node:
                print(node.val,level,len(res))
            if node and level == len(res):
                res.append(node.val)
                maxLevel = level
            if node:
                dfs(node.right,level+1)
                dfs(node.left,level+1)
        dfs(root,0)
        return res
