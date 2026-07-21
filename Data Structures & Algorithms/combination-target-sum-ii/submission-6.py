class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        nums = sorted(candidates)
        res, sol = [], []

        def dfs(start, total):
            #looping from zero = [1, 2] [2, 1] feasible - we dont want this
            #doing start + 1 in loop = [1, 2] [2, 1], only one is valid - we want this
            #doing start in loop = same element can be used unlimited
            #doing start + 1 = each element used at most once

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
        