class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        '''
        contains duplicates
        '''

        res, sol = [], []
        nums = candidates
        nums.sort()

        def dfs(start):
            if sum(sol) == target:
                res.append(sol[:])
                return

            if sum(sol) > target:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sol.append(nums[i])
                dfs(i + 1)
                sol.pop()

        dfs(0)
        return res


        