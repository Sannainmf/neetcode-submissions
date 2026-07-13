class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        r = len(nums) - 1

        index = 0

        def swap(l, r):
            t = nums[l]
            nums[l] = nums[r]
            nums[r] = t

        while index <= r:
            
            if nums[index] == 0:
                swap(l, index)
                l += 1
            
            elif nums[index] == 2:
                swap(r, index)
                r -= 1
                index -= 1
            index += 1
        
        return nums

    



        