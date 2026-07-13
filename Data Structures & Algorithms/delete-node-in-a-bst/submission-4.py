# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def minr(root): 
            """right pred"""

            if not root or not root.left:
                return root

            return minr(root.left)

        
        def delete(root, key):
            if not root:
                return

            if key < root.val:
                root.left = delete(root.left, key)
            elif key > root.val:
                root.right = delete(root.right, key)
            else:

                if not root.left and not root.right:
                    return None
                elif root.left and not root.right:
                    return root.left
                elif root.right and not root.left:
                    return root.right
                else:
                    rightMin = minr(root.right)
                    root.val = rightMin.val
                    root.right = delete(root.right, rightMin.val)

            return root

        return delete(root, key)



            

        
        