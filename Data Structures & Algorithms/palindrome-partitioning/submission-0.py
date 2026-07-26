class Solution:
    def partition(self, s: str) -> List[List[str]]:

        """
        
        """

        res, sol = [], []

        def dfs(i):
            if i >= len(s):
                res.append(sol[:])
                return

            for j in range(i, len(s)):
                part = s[i:j + 1]
                if part == part[::-1]:
                    sol.append(part)
                    dfs(j + 1)
                    sol.pop()

        dfs(0)
        return res



        