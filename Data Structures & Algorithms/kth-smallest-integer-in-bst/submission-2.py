# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        """
        in order traversal?

        basically we go until we hit the end, if its a num, add to array.
        when array length is k return arr[-1]
        """
        arr = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)

            if len(arr) < k:
                arr.append(root.val)

            dfs(root.right)

        dfs(root)
        return arr[-1]





        