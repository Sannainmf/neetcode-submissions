# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        in order for them to be balanced, difference in height needs to be <= 1.
        If greater than 1, it is false.

        A global variable set at the beginning to True - as we go through
        the tree, if we every calculate difference in height where it is
        greater than > 1, we change global var to False. And then we reutrn False once
        DFS ends.
        """

        balanced = [True]

        def dfs(root):
            if not root:
                return 0

            left_height = dfs(root.left)
            right_height = dfs(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False

            return 1 + max(left_height, right_height)

        dfs(root)
        return balanced[0]


            


