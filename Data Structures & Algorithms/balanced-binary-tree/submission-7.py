# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        """post order"""

        b = [True]

        def dfs(root):
            if not root:
                return 0
 
            l = dfs(root.left) + 1
            r = dfs(root.right) + 1

            if abs(l - r) > 1:
                b[0] = False

            return max(l, r)

        dfs(root)
        return b[0]

            


        