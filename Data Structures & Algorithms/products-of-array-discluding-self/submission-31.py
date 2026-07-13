class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        arr = []

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    prod = prod * nums[j]

            arr.append(prod)

        return arr

        