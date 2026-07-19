class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        """
        have a global variable outside dfs func

        if i == len(nums):
            total += sol[-1]
            return

        dfs(i + 1)

        if not sol:
            sol.append(nums[i])
        else:
            sol.append(sol[-1] ^ nums[i])

        dfs(i + 1)
        sol.pop()
        """

        res = [0]
        n = len(nums)

        def dfs(i, total):
            res[0] += total

            for j in range(i, len(nums)):
                total ^= nums[j]
                dfs(j + 1, total)
                total ^= nums[j]
        
        dfs(0, 0)
        return res[0]
                

            


        

        

        
        