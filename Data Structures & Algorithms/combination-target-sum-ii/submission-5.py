class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res, sol = [], []
        nums = sorted(candidates)
        def dfs(start, total):
        # without i + 1 (simply loop), we are appending [1, 2] [2, 1] - both feasible

        # with loop, dfs(i + 1), we [1, 2] [2, 1] are the same, and only one can be used

        # dfs(i), we can reuse same element

        # dfs(i + 1) we use element at most once
            if total == target:
                res.append(sol[:])
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sol.append(nums[i])
                dfs(i + 1, total + nums[i])
                sol.pop()

        dfs(0, 0)
        return res





        