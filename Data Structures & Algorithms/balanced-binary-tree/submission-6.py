# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0

            l = dfs(root.left) + 1
            r = dfs(root.right) + 1

            difference = abs(l - r)

            if l == 0 or r == 0:
                return -1

            if difference > 1:
                return -1

            return max(l, r)

        return dfs(root) != -1
            

            
        