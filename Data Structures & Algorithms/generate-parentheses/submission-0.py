class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res, stack = [], []
        string = []

        c, o = 0, 0

        def dfs(o, c):
            if len(string) == n * 2:
                res.append(''.join(string)[:])

            if o < n:
                string.append('(')
                dfs(o + 1, c)
                string.pop()
            
            if c < o:
                string.append(')')
                dfs(o, c +  1)
                string.pop()

        dfs(0, 0)
        return res
                



            





        