class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hsh = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        if digits == "":
            return []

        res, sol = [], []

        def dfs(index):
            if len(sol) == len(digits):
                res.append(''.join(sol[:]))
                return

            for char in hsh[digits[index]]:
                sol.append(char)
                dfs(index + 1)
                sol.pop()

        dfs(0)
        return res
