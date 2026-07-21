class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        total = [0]

        def dfs(start, curr):
            total[0] += curr

            for i in range(start, len(nums)):
                curr ^= nums[i]
                dfs(i + 1, curr)
                curr ^= nums[i]

        dfs(0, 0)
        return total[0]


        