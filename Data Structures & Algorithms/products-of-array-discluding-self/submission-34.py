class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        numsl = [0] * len(nums)
        numsr = [0] * len(nums)
        l, r = 1, 1

        for i in range(len(nums)):

            j = -i - 1

            numsl[i] = l
            numsr[j] = r
            l *= nums[i]
            r *= nums[j]
            
        return [i * j for i, j in zip(numsl, numsr)]
        

        