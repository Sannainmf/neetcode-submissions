class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        arr = []
        product = 1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    product = product * nums[j]
                else:
                    continue
            
            arr.append(product)
            product = 1

        return arr


             
        