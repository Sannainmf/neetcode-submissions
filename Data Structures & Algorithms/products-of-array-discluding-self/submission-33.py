class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l_element = 1
        r_element = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n 

        for i in range(len(nums)):
            j = -i -1 

            l_arr[i] = l_element
            r_arr[j] = r_element
            l_element = l_element * nums[i]
            r_element = r_element * nums[j]

        return [i * j for i, j in zip(l_arr, r_arr)]
        