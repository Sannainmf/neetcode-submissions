class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n
        l_element = 1
        r_element = 1
        
        for i in range(len(nums)):
            j = -i - 1

            l_arr[i] = l_element
            r_arr[j] = r_element
            l_element *= nums[i]
            r_element *= nums[j]

        return [i * j for i,j in zip(l_arr, r_arr)]