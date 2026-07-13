# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        """
        breadth first search, keep track of levels, append right most value at each level
        """

        if not root:
            return []

        q = deque()
        q.append(root)
        r = []

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            r.append(level[len(level) - 1])

        return r

        