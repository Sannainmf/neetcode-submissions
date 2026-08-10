class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        if we loop from zero each time, we can use a number infinite number of times

        if start = i, we can use 

        if start = i + 1, we use each number once
        """

        res, sol = [], []
        nums.sort()

        def dfs(start):
            res.append(sol[:])

            for i in range(start, len(nums)):
                if i > start and nums[i - 1] == nums[i]:
                    continue
                sol.append(nums[i])
                dfs(i + 1)
                sol.pop()

        dfs(0)
        return res