# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node :
                return
            dfs(node.left)
            self.result= min(self.result,node.val-self.prev)
            self.prev=node.val
            dfs(node.right)
        self.prev = float("-inf")
        self.result= float ("inf")
        dfs(root)
        return self.result
            
