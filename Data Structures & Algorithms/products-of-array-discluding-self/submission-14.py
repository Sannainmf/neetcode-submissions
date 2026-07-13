class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        arr = []
        prod = 1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    prod = prod * nums[j]
                
            arr.append(prod)
            prod = 1

        return arr
             
        