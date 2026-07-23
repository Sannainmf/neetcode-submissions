class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        """
        given array positive int nums, and pos int target

        return minimal length of subarray whose sum is greater than or equal to target
        if no such, return 0

        - sliding window
        """

        l = 0
        total = 0
        length = float('inf')
        
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                length = min(length, r - l + 1)
                total -= nums[l]
                l += 1

        if length == float('inf'):
            return 0
        else:
            return length




        
        