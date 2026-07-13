# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        """
        root and target, delete all leaf nodes with value target.

        post order
        """

        def delete(root):
            if not root:
                return None

            root.left = delete(root.left)
            root.right = delete(root.right)

            if root.val == target and not root.left and not root.right:
                return None

            return root

        return delete(root)

            

        