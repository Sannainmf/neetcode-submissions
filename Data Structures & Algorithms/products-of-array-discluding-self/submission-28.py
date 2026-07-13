class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        arr = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    product = product * nums[j]

            arr.append(product)
            product = 1


        return arr


                
            






        






        