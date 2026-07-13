# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        num = [0]
    
        def dfs(root, m):
            if not root:
                return

            if root.val >= m:
                num[0] += 1

            m = max(root.val, m)
            
            dfs(root.left, m)
            dfs(root.right, m)

            return
        
        dfs(root, root.val)
        return num[0]

            
        