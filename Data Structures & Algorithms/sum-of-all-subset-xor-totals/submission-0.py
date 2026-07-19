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

        total = [0]
        sol = []

        def dfs(i):
            if i == len(nums):
                if sol:
                    total[0] += sol[-1]
                return

            dfs(i + 1)

            if not sol:
                sol.append(nums[i])
            else:
                sol.append(sol[-1] ^ nums[i])

            dfs(i + 1)
            sol.pop()

        dfs(0)
        return total[0]


        

        

        
        