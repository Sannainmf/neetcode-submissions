class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        sol = []

        def dfs(i):
            res.append(sol[:])
    

            for j in range(i, len(nums)):
                sol.append(nums[j])
                dfs(j + 1)
                sol.pop()

        dfs(0)
        return res

        