# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque()
        q.append(root)
        res = []

        if not root:
            return []

        while q:
            level = []
            for i in range(len(q)):
                t = q.popleft()
                level.append(t.val)

                if t.left:
                    q.append(t.left)

                if t.right:
                    q.append(t.right)

            res.append(level)


        return res

        