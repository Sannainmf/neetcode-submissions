class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res, sol = [], []
        used = [False] * len(nums)

        def dfs():
            if len(sol) == len(nums):
                res.append(sol[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                sol.append(nums[i])
                dfs()
                sol.pop()
                used[i] = False

        dfs()
        return res
        