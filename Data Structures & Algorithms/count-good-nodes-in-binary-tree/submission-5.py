# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        """
        we start at root,

        root ar start is baseline.

        if curr.val > m (max)
            count += 1
        m = max(curr.val, m)
        func(root.left, m)
        func(root.right, m)
        """
        count = [0]

        def gNodes(root, m):
            if not root:
                return

            if root.val >= m:
                count[0] += 1

            m = max(m, root.val)

            gNodes(root.left, m)
            gNodes(root.right, m)

            return

        gNodes(root, root.val)
        return count[0]
                