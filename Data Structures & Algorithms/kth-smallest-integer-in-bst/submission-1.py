# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        """
        This uses some inorder BST
        """

        index = [0]
        node = [0]

        def inOrder(root):
            if not root:
                return None

            inOrder(root.left)

            index[0] += 1
            if index[0] == k:
                node[0] = root.val
            
            inOrder(root.right)

            return node[0]

        inOrder(root)
        return node[0]

             