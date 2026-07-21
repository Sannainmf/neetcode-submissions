class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res, sol = [], []
        nums.sort()

        def dfs(start):
            res.append(sol[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sol.append(nums[i])
                dfs(i + 1)
                sol.pop()

        dfs(0)
        return res
        