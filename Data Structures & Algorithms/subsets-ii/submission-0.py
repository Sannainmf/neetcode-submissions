class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sol = []

        def dfs(i):
            if sorted(sol) not in res:
                res.append(sorted(sol[:]))

            for j in range(i, len(nums)):
                sol.append(nums[j])
                dfs(j + 1)
                sol.pop()

        dfs(0)
        return res