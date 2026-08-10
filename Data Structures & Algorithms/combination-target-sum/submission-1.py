class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res, sol = [], []

        def dfs(start):
            if sum(sol) == target:
                res.append(sol[:])
                return

            if sum(sol) > target:
                return

            for i in range(start, len(nums)):
                sol.append(nums[i])
                dfs(i)
                sol.pop()

        dfs(0)
        return res
        