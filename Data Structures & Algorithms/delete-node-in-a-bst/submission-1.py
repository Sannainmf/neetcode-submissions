# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def min(root):
            if not root or not root.left:
                return root

            return min(root.left)


        def delete(root, key):
            if not root:
                return

            if key < root.val:
                root.left = delete(root.left, key)
            elif key > root.val:
                root.right = delete(root.right, key)
            else:

                """
                few conditions:
                    1. if the root doesnt have any children, simply return
                    2. if the root has left or right, return whichever exists
                    3. if root has both, find lowest value in right subtree, delete that node
                    return that node.
                """

                if not root.left and not root.right:
                    return None
                
                if not root.left:
                    return root.right
                
                if not root.right:
                    return root.left

                if root.left and root.right:
                    m = min(root.right)
                    root.val = m.val
                    root.right = delete(root.right, m.val)

            return root

        return delete(root, key)

        