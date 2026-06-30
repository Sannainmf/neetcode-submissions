class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        """
        simply do binary search, if target found return index, if not return where it would be
        """
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1

        return l

        
