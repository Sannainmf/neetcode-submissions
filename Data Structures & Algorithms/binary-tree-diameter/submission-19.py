# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        """
        post order
        """

        diam = [0]

        def dfs(root):

            if not root:
                return -1

            left = dfs(root.left) + 1
            right = dfs(root.right) + 1

            d = left + right
            diam[0] = max(diam[0], d)

            return max(left, right)

        dfs(root)
        return diam[0]



        