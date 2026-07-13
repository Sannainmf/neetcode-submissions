# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        """
        implement a preorder traversal. Process node, track the max, if the current node
        is >= the max, we can increment a counter. Otherwisie do nothing.
        """

        count = [0]
        m = float('-inf')

        def good(root, m):
            if not root:
                return 

            if root.val >= m:
                count[0] += 1
            
            maxi = max(root.val, m)

            good(root.left, maxi)
            good(root.right, maxi)

            return

        good(root, m)
        return count[0]


        