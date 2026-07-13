# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        """
        traverse thru tree, if we find node with same value as subroot value, 
        we can do left right traverse for both and if theyre both None, return True,
        if None or, return false

        two methods. one finds start value, calls the other to check
        """

        def sameTree(p, q):

            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            else:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        def dfs(root):
            if not root:
                return False
            
            if sameTree(root, subRoot):
                return True

            return dfs(root.left) or dfs(root.right)

        return dfs(root)
        
                


        