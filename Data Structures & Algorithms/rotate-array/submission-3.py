class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        2 pointers. left pointer will be 0, right will be k.
        l and r swap, increment both
        """

        """
        start at the end, loop until k is 0.
        """

        k = k % len(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
            t = nums[l]
            nums[l] = nums[r]
            nums[r] = t
            l += 1
            r -= 1
        
        l = 0
        r = k - 1
        while l < r:
            t = nums[l]
            nums[l] = nums[r]
            nums[r] = t
            l += 1
            r -= 1

        l = k
        r = len(nums) - 1
        while l < r:
            t = nums[l]
            nums[l] = nums[r]
            nums[r] = t
            l += 1
            r -= 1

        


        




        