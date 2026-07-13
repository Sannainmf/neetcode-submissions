class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        """
        given array positive int nums, and pos int target

        return minimal length of subarray whose sum is greater than or equal to target
        if no such, return 0

        - sliding window
        """

        l = 0
        r = 0

        total = 0
        tracker = float('inf')

        while r < len(nums):
            total += nums[r]
            
            while total >= target:
                tracker = min(tracker, r - l + 1)
                total -= nums[l]
                l += 1

            if total < target:
                r += 1

        if tracker == float('inf'):
            return 0
        else:
            return tracker





        
        