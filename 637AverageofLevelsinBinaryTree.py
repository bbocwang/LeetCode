# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return [0]
        levelsum = {0:root.val}
        count = {0:1}
        res = []
        def dfs(node,level):
            if node.left:
                levelsum[level+1] = levelsum.get(level+1,0)+node.left.val
                count[level+1] = count.get(level+1,0)+1
                dfs(node.left,level+1)
            if node.right:
                levelsum[level+1] = levelsum.get(level+1,0)+node.right.val
                count[level+1] = count.get(level+1,0)+1
                dfs(node.right,level+1)
            
        dfs(root,0)
        for i in levelsum:
                avg = levelsum.get(i)/float(count.get(i))
                res.append(avg)
        return res
