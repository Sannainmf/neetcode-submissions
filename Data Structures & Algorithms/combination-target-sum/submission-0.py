class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        """
        given array of distinct integer

        and target integer

        task is to return a list of all unique combinations of nums (rec bt)
        where the chosen numbers sum to target

        the same number may be chosen from nums unlimited number of times, 
        two combinations r the same if the frequency of the chose numbers
        is the same, otherwise they are different

        you may return thr combinations in any order and the order
        of the number in each combination can be in any order

        """

        # base case will be if _ sums to target

        res, sol = [], []

        def dfs(start, total):
            if total == target:
                res.append(sol[:])
                return

            if total > target:
                return
            for i in range(start, len(nums)):
                sol.append(nums[i])
                dfs(i, total + nums[i])
                sol.pop()

        dfs(0, 0)
        return res
                

        

        

        