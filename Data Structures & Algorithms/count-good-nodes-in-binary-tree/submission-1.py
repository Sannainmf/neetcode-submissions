# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        """
        at every node you need to check if the path from the root node didnt contain a number greater than the node
        ur currently at. If we go top -> bottom we wouldnt know the nodes after them, hence we would have to go
        bottom -> top, so we can back trace to the root. 
        """

        """
        we know to use preorder. If we process a node, we know its value. If the value is less than the max, its not good.
        if thje value is greater than the max, its good.
        """

        m = root.val
        count = [0]

        def rec(root, m):
            if not root:
                return

            if root.val >= m:
                count[0] += 1
            
            maxi = max(root.val, m)
            rec(root.left, maxi)
            rec(root.right, maxi)

            return

        rec(root, m)
        return count[0]
        
        