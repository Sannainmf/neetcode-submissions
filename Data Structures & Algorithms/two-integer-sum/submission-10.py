class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}

        for i, nums in enumerate(nums):
            comp = target - nums
            if comp in hash:
                return [hash[comp], i]
            
            hash[nums] = i


        
        