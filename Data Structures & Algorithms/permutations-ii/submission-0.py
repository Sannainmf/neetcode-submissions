class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        sol = []
        used = [False] * len(nums)
        nums.sort()

        def dfs():
            #permutations - so we want to loop from zero [1, 2] [2, 1] feasible
            if len(sol) == len(nums):
                res.append(sol[:])
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                if used[i]:
                    continue

                sol.append(nums[i])
                used[i] = True

                dfs()

                sol.pop()
                used[i] = False


        dfs()
        return res